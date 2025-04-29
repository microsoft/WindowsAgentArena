import json
import logging
import re
import base64
import os
from typing import Dict, List, Optional, Any, Tuple
from io import BytesIO
import time
from PIL import Image

try:
    from anthropic import Anthropic, AnthropicBedrock
except ImportError:
    Anthropic = None
    AnthropicBedrock = None

logger = logging.getLogger("desktopenv.agent")

class ClaudeAgent:
    """
    ClaudeAgent adapter for WindowsAgentArena
    
    This agent mimics Claude's Computer tool API and maps it to the existing Windows agent action space
    """
    def __init__(
            self,
            server: str = "anthropic",
            model: str = "claude-3-7-sonnet-20250219",
            temperature: float = 0.5,
    ):
        self.action_space = "code_block"
        self.server = server
        self.model = model
        self.temperature = temperature
        
        # Initialize the appropriate Anthropic client based on server
        self.client = None
        try:
            if server == "anthropic" and Anthropic:
                self.client = Anthropic()
                logger.info("Anthropic client initialized")
            elif server == "awsbedrock" and AnthropicBedrock:
                self.client = AnthropicBedrock()
                logger.info("AnthropicBedrock client initialized")
            else:
                logger.error(f"Unsupported server type: {server} or client library not available")
        except Exception as e:
            logger.error(f"Failed to initialize Anthropic client: {e}")
        
        # Define display dimensions for Claude's computer tool
        # Values from the XRES / YRES env variables in Dockerfile-WinArena
        self.display_width = 1440
        self.display_height = 900
        
        # Store previous screenshots and actions
        self.prev_actions = []
        self.last_image = None
        self.use_last_screen = True
        self.step_counter = 0
        
        # Memory for the agent
        self.memory_block_text_empty = """
```memory
# empty memory block
```
"""
        self.memory_block_text = self.memory_block_text_empty
        
        # Flag to detect task completion
        self.task_completed = False
        
    def computer_action_to_code(self, action: Dict) -> str:
        """
        Convert Claude's computer tool action to Windows Agent Arena Python code
        
        Args:
            action: The action from Claude's computer tool
            
        Returns:
            Python code to execute in WindowsAgentArena
        """
        action_type = action.get("type")
        
        if action_type == "screenshot":
            # Screenshot is handled by the environment, not needed in the code
            return "WAIT"
            
        elif action_type == "move_mouse":
            # Convert Claude's coordinates (relative to display) to WinArena's (0-1 normalized)
            x = action.get("x", 0) / self.display_width
            y = action.get("y", 0) / self.display_height
            return f"computer.mouse.move_abs({x}, {y})"
            
        elif action_type == "click":
            return "computer.mouse.single_click()"
            
        elif action_type == "double_click":
            return "computer.mouse.double_click()"
            
        elif action_type == "right_click":
            return "computer.mouse.right_click()"
            
        elif action_type == "scroll":
            direction = action.get("direction", "down").lower()
            if direction in ["up", "down"]:
                return f"computer.mouse.scroll(dir=\"{direction}\")"
            else:
                # Handle horizontal scrolling or unsupported directions
                return f"# Unsupported scroll direction: {direction}"
                
        elif action_type == "type":
            text = action.get("text", "")
            # Escape double quotes and backslashes in the text
            escaped_text = text.replace("\\", "\\\\").replace("\"", "\\\"")
            return f"computer.keyboard.write(\"{escaped_text}\")"
            
        elif action_type == "press_key":
            key = action.get("key", "")
            return f"computer.keyboard.press(\"{key}\")"
            
        elif action_type == "press_keys":
            keys = action.get("keys", [])
            # For combined keys like ctrl+c, convert to expected format
            if len(keys) > 1:
                key_combo = "+".join(keys)
                return f"computer.keyboard.press(\"{key_combo}\")"
            elif len(keys) == 1:
                return f"computer.keyboard.press(\"{keys[0]}\")"
            else:
                return "# No keys specified"
                
        elif action_type == "copy":
            return "computer.keyboard.press(\"ctrl+c\")"
            
        elif action_type == "paste":
            return "computer.clipboard.paste()"
            
        elif action_type == "maximize_window":
            return "computer.os.maximize_window()"
            
        elif action_type == "switch_application":
            app_name = action.get("application_name", "")
            return f"computer.window_manager.switch_to_application(\"{app_name}\")"
            
        elif action_type == "done":
            self.task_completed = True
            return "DONE"
            
        else:
            # Log unsupported actions
            logger.warning(f"Unsupported action type: {action_type}")
            return f"# Unsupported action: {action_type}"
    
    def generate_code_from_actions(self, actions: List[Dict]) -> str:
        """
        Generate code from a list of Claude's computer actions
        
        Args:
            actions: List of actions from Claude's computer tool
            
        Returns:
            Python code block to execute in WindowsAgentArena
        """
        code_lines = []
        
        # Process all actions
        for action in actions:
            code_line = self.computer_action_to_code(action)
            code_lines.append(code_line)
            
            # If the action is "done", stop processing
            if self.task_completed:
                break
                
        # Join all code lines
        code_block = "\n".join(code_lines)
        
        # Handle empty code blocks
        if not code_block.strip():
            code_block = "# No actions to execute"
            
        return code_block
        
    def encode_image_to_base64(self, image) -> str:
        """
        Encode PIL Image to base64 string
        
        Args:
            image: PIL Image object
            
        Returns:
            base64 encoded string
        """
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return img_str
    
    def call_claude_api(self, instruction: str, image, window_title: str, window_names_str: str) -> List[Dict]:
        """
        Call Claude API with the computer tool
        
        Args:
            instruction: The instruction from the user
            image: Screenshot of the current state
            window_title: Current window title
            window_names_str: List of window names
            
        Returns:
            A list of computer actions from Claude
        """
        if not self.client:
            error_msg = "Anthropic client not initialized. Please provide a valid API key."
            logger.error(error_msg)
            raise RuntimeError(error_msg)
            
        try:
            # Encode the image
            base64_image = self.encode_image_to_base64(image)
            
            # Create message content with instruction and image
            content = [
                {"type": "text", "text": f"Task: {instruction}\n\nCurrent window: {window_title}\n\nAvailable windows: {window_names_str}"},
                {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": base64_image}}
            ]
            
            # Determine tool type and beta flag based on model
            tool_type = "computer_20250124"  # Default for Claude 3.7 Sonnet
            beta_flag = "computer-use-2025-01-24"
            
            # Use appropriate tool type for Claude 3.5 Sonnet
            if "claude-3-5" in self.model:
                tool_type = "computer_20241022"
                beta_flag = "computer-use-2024-10-22"
            
            # Define the computer tool
            tools = [
                {
                    "type": tool_type,
                    "name": "computer",
                    "display_width_px": self.display_width,
                    "display_height_px": self.display_height,
                    "display_number": 1
                }
            ]
            
            # Make API call
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                temperature=self.temperature,
                messages=[{"role": "user", "content": content}],
                tools=tools,
                betas=[beta_flag]
            )
            
            # Parse the response to extract computer actions
            actions = []
            for content_block in response.content:
                if content_block.type == "tool_use" and content_block.name == "computer":
                    # Extract the computer action
                    action = content_block.input
                    actions.append(action)
            
            if not actions:
                error_msg = "No computer actions returned from Claude API"
                logger.error(error_msg)
                raise RuntimeError(error_msg)
                
            return actions
            
        except Exception as e:
            logger.error(f"Error calling Claude API: {e}")
            raise
    
    def predict(self, instruction: str, obs: Dict) -> Tuple[str, List[str], Dict, Dict]:
        """
        Predict the next action(s) based on the current observation.
        
        Args:
            instruction: The instruction from the user
            obs: The observation from the environment
            
        Returns:
            A tuple of (response, actions, logs, computer_update_args)
        """
        start_time = time.time()
        logs = {}
        
        # Extract observation data
        image_file = BytesIO(obs['screenshot'])
        view_image = Image.open(image_file)
        view_rect = [0, 0, view_image.width, view_image.height]
        
        window_title = obs['window_title']
        window_names_str = obs['window_names_str']
        window_rect = obs['window_rect']
        computer_clipboard = obs['computer_clipboard']
        
        original_h, original_w = view_image.height, view_image.width
        
        # Store the current image for future reference
        if self.use_last_screen:
            self.last_image = view_image
        
        # Log observation details
        logs['window_title'] = window_title
        logs['window_names_str'] = window_names_str
        logs['computer_clipboard'] = computer_clipboard
        logs['image_width'] = view_image.width
        logs['image_height'] = view_image.height
        
        # Get actions from Claude API
        claude_actions = self.call_claude_api(instruction, view_image, window_title, window_names_str)
        
        # Convert actions to code
        code_result = self.generate_code_from_actions(claude_actions)
        
        # Format the code for the WinArena environment
        plan_result = f"```python\n{code_result}\n```"
        
        # Log the plan
        logs['plan_result'] = plan_result
        
        # Extract the code block from the plan
        code_block = re.search(r'```python\n(.*?)```', plan_result, re.DOTALL)
        if code_block:
            code_block_text = code_block.group(1)
            actions = [code_block_text]
        else:
            logger.error("Plan not found")
            code_block_text = "# plan not found"
            actions = ["# plan not found"]
        
        # Store the action for future reference
        self.prev_actions.append(code_block_text)
        
        # Prepare computer update arguments
        scale = (original_w/view_image.width, original_h/view_image.height)
        computer_update_args = {
            'rects': [],  # No rects since we're using absolute coordinates
            'window_rect': view_rect,
            'screenshot': view_image,
            'scale': scale,
            'clipboard_content': computer_clipboard,
            'swap_ctrl_alt': False
        }
        
        self.step_counter += 1
        
        # Handle task completion
        if self.task_completed:
            actions = ["DONE"]
        
        response = ""
        return response, actions, logs, computer_update_args
    
    def reset(self):
        """Reset the agent state"""
        self.memory_block_text = self.memory_block_text_empty
        self.prev_actions = []
        self.last_image = None
        self.step_counter = 0
        self.task_completed = False
