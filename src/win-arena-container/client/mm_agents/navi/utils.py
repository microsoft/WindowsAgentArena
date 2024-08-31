
import easyocr # if this import is below transformers then transformers will randomly raise a segfault when loading blip2, don't move this line!!!

# import os
# os.environ['OPENBLAS_NUM_THREADS'] = '5'

from ultralytics import YOLO
import os
import io
import base64
import time
from PIL import Image, ImageDraw, ImageFont
import json
import requests
# # utility function
import os


import torchvision.transforms as T

import json
import sys
import os
import cv2
import numpy as np
# # %matplotlib inline
# from matplotlib import pyplot as plt
from transformers import Blip2Processor, Blip2ForConditionalGeneration

# import time
# import base64

# import os
# import ast
import torch
from typing import Tuple, List
from torchvision.ops import box_convert
import re
import supervision as sv
from ultralytics import YOLO

# import easyocr

reader = None
# reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory # 'ch_sim',

def get_parsed_content_icon(filtered_boxes, ocr_bbox, image_source, caption_model_processor):
    from PIL import Image
    to_tensor = T.ToTensor()
    to_pil = T.ToPILImage()
    
    # Convert image_source to tensor if it's a PIL image
    if isinstance(image_source, Image.Image):
        image_source = to_tensor(image_source.convert("RGB")).permute(1, 2, 0).numpy()

    # Ensure the image data is in uint8 format
    if image_source.dtype == np.float32:
        image_source = (image_source * 255).astype(np.uint8)

    if ocr_bbox:
        non_ocr_boxes = filtered_boxes[len(ocr_bbox):]
    else:
        non_ocr_boxes = filtered_boxes
    
    cropped_pil_image = []
    height, width, _ = image_source.shape
    for i, coord in enumerate(non_ocr_boxes):
        xmin = max(0, int(coord[0] * width))
        xmax = min(width, int(coord[2] * width))
        ymin = max(0, int(coord[1] * height))
        ymax = min(height, int(coord[3] * height))

        cropped_image = image_source[ymin:ymax, xmin:xmax, :]
        cropped_pil_image.append(to_pil(cropped_image))

    # import pdb; pdb.set_trace()
    prompt = "The image shows"
    model, processor = caption_model_processor['model'], caption_model_processor['processor']

    batch_size = 10  # Number of samples per batch
    generated_texts = []
    device = model.device

    for i in range(0, len(cropped_pil_image), batch_size):
        batch = cropped_pil_image[i:i+batch_size]
        if model.device == 'cuda':
            inputs = processor(images=batch, text=[prompt]*len(batch), return_tensors="pt").to(device=device, dtype=torch.float16)
        else:
            inputs = processor(images=batch, text=[prompt]*len(batch), return_tensors="pt").to(device=device)

        generated_ids = model.generate(**inputs, max_length=100, num_beams=5, no_repeat_ngram_size=2, early_stopping=True, num_return_sequences=1) # temperature=0.01, do_sample=True,
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)
        generated_text = [gen.strip() for gen in generated_text]
        generated_texts.extend(generated_text)

    return generated_texts



def get_parsed_content_icon_phi3v(filtered_boxes, ocr_bbox, image_source, caption_model_processor):
    to_pil = T.ToPILImage()
    if ocr_bbox:
        non_ocr_boxes = filtered_boxes[len(ocr_bbox):]
    else:
        non_ocr_boxes = filtered_boxes
    croped_pil_image = []
    for i, coord in enumerate(non_ocr_boxes):
        xmin, xmax = int(coord[0]*image_source.shape[1]), int(coord[2]*image_source.shape[1])
        ymin, ymax = int(coord[1]*image_source.shape[0]), int(coord[3]*image_source.shape[0])
        cropped_image = image_source[ymin:ymax, xmin:xmax, :]
        croped_pil_image.append(to_pil(cropped_image))

    model, processor = caption_model_processor['model'], caption_model_processor['processor']
    device = model.device
    messages = [{"role": "user", "content": "<|image_1|>\ndescribe the icon in one sentence"}] 
    prompt = processor.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    batch_size = 5  # Number of samples per batch
    generated_texts = []

    for i in range(0, len(croped_pil_image), batch_size):
        images = croped_pil_image[i:i+batch_size]
        image_inputs = [processor.image_processor(x, return_tensors="pt") for x in images]
        inputs ={'input_ids': [], 'attention_mask': [], 'pixel_values': [], 'image_sizes': []}
        texts = [prompt] * len(images)
        for i, txt in enumerate(texts):
            input = processor._convert_images_texts_to_inputs(image_inputs[i], txt, return_tensors="pt")
            inputs['input_ids'].append(input['input_ids'])
            inputs['attention_mask'].append(input['attention_mask'])
            inputs['pixel_values'].append(input['pixel_values'])
            inputs['image_sizes'].append(input['image_sizes'])
        max_len = max([x.shape[1] for x in inputs['input_ids']])
        for i, v in enumerate(inputs['input_ids']):
            inputs['input_ids'][i] = torch.cat([processor.tokenizer.pad_token_id * torch.ones(1, max_len - v.shape[1], dtype=torch.long), v], dim=1)
            inputs['attention_mask'][i] = torch.cat([torch.zeros(1, max_len - v.shape[1], dtype=torch.long), inputs['attention_mask'][i]], dim=1)
        inputs_cat = {k: torch.concatenate(v).to(device) for k, v in inputs.items()}

        generation_args = { 
            "max_new_tokens": 25, 
            "temperature": 0.01, 
            "do_sample": False, 
        } 
        generate_ids = model.generate(**inputs_cat, eos_token_id=processor.tokenizer.eos_token_id, **generation_args) 
        # # remove input tokens 
        generate_ids = generate_ids[:, inputs_cat['input_ids'].shape[1]:]
        response = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)
        response = [res.strip('\n').strip() for res in response]
        generated_texts.extend(response)

    return generated_texts

def remove_overlap(boxes, iou_threshold, ocr_bbox=None):
    assert ocr_bbox is None or isinstance(ocr_bbox, List)

    def box_area(box):
        return (box[2] - box[0]) * (box[3] - box[1])

    def intersection_area(box1, box2):
        x1 = max(box1[0], box2[0])
        y1 = max(box1[1], box2[1])
        x2 = min(box1[2], box2[2])
        y2 = min(box1[3], box2[3])
        return max(0, x2 - x1) * max(0, y2 - y1)

    def IoU(box1, box2):
        intersection = intersection_area(box1, box2)
        union = box_area(box1) + box_area(box2) - intersection
        if box_area(box1) > 0 and box_area(box2) > 0:
            ratio1 = intersection / box_area(box1)
            ratio2 = intersection / box_area(box2)
        else:
            ratio1, ratio2 = 0, 0
        return max(intersection / union, ratio1, ratio2)

    boxes = boxes.tolist()
    filtered_boxes = []
    if ocr_bbox:
        filtered_boxes.extend(ocr_bbox)
    # print('ocr_bbox!!!', ocr_bbox)
    for i, box1 in enumerate(boxes):
        # if not any(IoU(box1, box2) > iou_threshold and box_area(box1) > box_area(box2) for j, box2 in enumerate(boxes) if i != j):
        is_valid_box = True
        for j, box2 in enumerate(boxes):
            if i != j and IoU(box1, box2) > iou_threshold and box_area(box1) > box_area(box2):
                is_valid_box = False
                break
        if is_valid_box:
            # add the following 2 lines to include ocr bbox
            if ocr_bbox:
                if not any(IoU(box1, box3) > iou_threshold for k, box3 in enumerate(ocr_bbox)):
                    filtered_boxes.append(box1)
            else:
                filtered_boxes.append(box1)
    return torch.tensor(filtered_boxes)

def load_image(image_path: str) -> Tuple[np.array, torch.Tensor]:
    transform = T.Compose(
        [
            T.RandomResize([800], max_size=1333),
            T.ToTensor(),
            T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]
    )
    image_source = Image.open(image_path).convert("RGB")
    image = np.asarray(image_source)
    image_transformed, _ = transform(image_source, None)
    return image, image_transformed


def annotate(image_source: np.ndarray, boxes: torch.Tensor, logits: torch.Tensor, phrases: List[str], text_scale: float, 
             text_padding=5, text_thickness=2, thickness=3) -> np.ndarray:
    """    
    This function annotates an image with bounding boxes and labels.

    Parameters:
    image_source (np.ndarray): The source image to be annotated.
    boxes (torch.Tensor): A tensor containing bounding box coordinates. in cxcywh format, pixel scale
    logits (torch.Tensor): A tensor containing confidence scores for each bounding box.
    phrases (List[str]): A list of labels for each bounding box.
    text_scale (float): The scale of the text to be displayed. 0.8 for mobile/web, 0.3 for desktop # 0.4 for mind2web

    Returns:
    np.ndarray: The annotated image.
    """
    h, w, _ = image_source.shape
    boxes = boxes * torch.Tensor([w, h, w, h])
    xyxy = box_convert(boxes=boxes, in_fmt="cxcywh", out_fmt="xyxy").numpy()
    xywh = box_convert(boxes=boxes, in_fmt="cxcywh", out_fmt="xywh").numpy()
    detections = sv.Detections(xyxy=xyxy)

    labels = [f"{phrase}" for phrase in range(boxes.shape[0])]

    # from util.box_annotator import BoxAnnotator 
    box_annotator = BoxAnnotator(text_scale=text_scale, text_padding=text_padding,text_thickness=text_thickness,thickness=thickness) # 0.8 for mobile/web, 0.3 for desktop # 0.4 for mind2web
    annotated_frame = image_source.copy()
    annotated_frame = box_annotator.annotate(scene=annotated_frame, detections=detections, labels=labels, image_size=(w,h))

    label_coordinates = {f"{phrase}": v for phrase, v in zip(phrases, xywh)}
    return annotated_frame, label_coordinates


def predict(model, image, caption, box_threshold, text_threshold):
    """ Use huggingface model to replace the original model
    """
    model, processor = model['model'], model['processor']
    device = model.device

    inputs = processor(images=image, text=caption, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model(**inputs)

    results = processor.post_process_grounded_object_detection(
        outputs,
        inputs.input_ids,
        box_threshold=box_threshold, # 0.4,
        text_threshold=text_threshold, # 0.3,
        target_sizes=[image.size[::-1]]
    )[0]
    boxes, logits, phrases = results["boxes"], results["scores"], results["labels"]
    return boxes, logits, phrases


def predict_yolo(model, image_path, box_threshold):
    """ Use huggingface model to replace the original model
    """
    # model = model['model']
    device = model.device
    result = model.predict(
    source=image_path,
    conf=box_threshold,
    device=device,
    # iou=0.5, # default 0.7
    )
    boxes = result[0].boxes.xyxy#.tolist() # in pixel space
    print('boxes', boxes.device)
    conf = result[0].boxes.conf
    phrases = [str(i) for i in range(len(boxes))]

    return boxes, conf, phrases


def get_som_labeled_img(img_path, model=None, BOX_TRESHOLD = 0.01, output_coord_in_ratio=False, ocr_bbox=None, text_scale=0.4, text_padding=5, draw_bbox_config=None, caption_model_processor=None, ocr_text=[], use_local_semantics=True):
    """ ocr_bbox: list of xyxy format bbox
    """
    TEXT_PROMPT = "clickable buttons on the screen"
    # BOX_TRESHOLD = 0.02 # 0.05/0.02 for web and 0.1 for mobile
    TEXT_TRESHOLD = 0.01 # 0.9 # 0.01
    image_source = Image.open(img_path).convert("RGB")
    w, h = image_source.size
    # import pdb; pdb.set_trace()
    if not isinstance(model, YOLO): # TODO
        xyxy, logits, phrases = predict(model=model, image=image_source, caption=TEXT_PROMPT, box_threshold=BOX_TRESHOLD, text_threshold=TEXT_TRESHOLD)
    else:
        xyxy, logits, phrases = predict_yolo(model=model, image_path=img_path, box_threshold=BOX_TRESHOLD)
    xyxy = xyxy / torch.Tensor([w, h, w, h]).to(xyxy.device)
    image_source = np.asarray(image_source)
    phrases = [str(i) for i in range(len(phrases))]

    # annotate the image with labels
    h, w, _ = image_source.shape
    if ocr_bbox:
        ocr_bbox = torch.tensor(ocr_bbox) / torch.Tensor([w, h, w, h])
        ocr_bbox=ocr_bbox.tolist()
    else:
        print('no ocr bbox!!!')
        ocr_bbox = None
    filtered_boxes = remove_overlap(boxes=xyxy, iou_threshold=0.9, ocr_bbox=ocr_bbox)
    
    # get parsed icon local semantics
    if use_local_semantics:
        caption_model = caption_model_processor['model']
        if 'phi3_v' in caption_model.config.model_type: 
            parsed_content_icon = get_parsed_content_icon_phi3v(filtered_boxes, ocr_bbox, image_source, caption_model_processor)
        else:
            parsed_content_icon = get_parsed_content_icon(filtered_boxes, ocr_bbox, image_source, caption_model_processor)
        ocr_text = [f"Text Box ID {i}: {txt}" for i, txt in enumerate(ocr_text)]
        icon_start = len(ocr_text)
        parsed_content_icon_ls = []
        for i, txt in enumerate(parsed_content_icon):
            parsed_content_icon_ls.append(f"Icon Box ID {str(i+icon_start)}: {txt}")
        parsed_content_merged = ocr_text + parsed_content_icon_ls
    else:
        ocr_text = [f"Text Box ID {i}: {txt}" for i, txt in enumerate(ocr_text)]
        parsed_content_merged = ocr_text

    filtered_boxes = box_convert(boxes=filtered_boxes, in_fmt="xyxy", out_fmt="cxcywh")

    phrases = [i for i in range(len(filtered_boxes))]
    
    # draw boxes
    if draw_bbox_config:
        annotated_frame, label_coordinates = annotate(image_source=image_source, boxes=filtered_boxes, logits=logits, phrases=phrases, **draw_bbox_config)
    else:
        annotated_frame, label_coordinates = annotate(image_source=image_source, boxes=filtered_boxes, logits=logits, phrases=phrases, text_scale=text_scale, text_padding=text_padding)
    
    pil_img = Image.fromarray(annotated_frame)
    buffered = io.BytesIO()
    pil_img.save(buffered, format="PNG")
    encoded_image = base64.b64encode(buffered.getvalue()).decode('ascii')
    if output_coord_in_ratio:
        # h, w, _ = image_source.shape
        label_coordinates = {k: [v[0]/w, v[1]/h, v[2]/w, v[3]/h] for k, v in label_coordinates.items()}
        assert w == annotated_frame.shape[1] and h == annotated_frame.shape[0]

    return encoded_image, label_coordinates, parsed_content_merged


def get_xywh(input):
    x, y, w, h = input[0][0], input[0][1], input[2][0] - input[0][0], input[2][1] - input[0][1]
    x, y, w, h = int(x), int(y), int(w), int(h)
    return x, y, w, h

def get_xyxy(input):
    x, y, xp, yp = input[0][0], input[0][1], input[2][0], input[2][1]
    x, y, xp, yp = int(x), int(y), int(xp), int(yp)
    return x, y, xp, yp

def get_xywh_yolo(input):
    x, y, w, h = input[0], input[1], input[2] - input[0], input[3] - input[1]
    x, y, w, h = int(x), int(y), int(w), int(h)
    return x, y, w, h
    


def call_gpt4v_new(message_text, image_path=None, max_tokens=2048):
    if image_path:
        try:
            with open(image_path, "rb") as img_file:
                encoded_image = base64.b64encode(img_file.read()).decode('ascii')
        except: 
            encoded_image = image_path
    
    if image_path:
        content = [{"type": "image_url","image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}, {"type": "text","text": message_text},]
    else:
        content = [{"type": "text","text": message_text},]

    max_num_trial = 3
    num_trial = 0
    call_api_success = True

    # endpoint = "https://yadaoai.openai.azure.com/"
    # # deployment = "dataoai2-gpt4"
    # deployment = 'gpt-4o'
    # token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")
    # client = AzureOpenAI(
    #     azure_endpoint=endpoint,
    #     azure_ad_token_provider=token_provider,
    #     api_version="2024-02-01",
    # )
    while num_trial < max_num_trial:
        try:
            response = client.chat.completions.create(
                            model=deployment,
                            messages=[
                                        {
                                        "role": "system",
                                        "content": [
                                            {
                                            "type": "text",
                                            "text": "You are an AI assistant that is good at making plans and analyzing screens, and helping people find information."
                                            },
                                        ]
                                        },
                                        {
                                        "role": "user",
                                        "content": content
                                        }
                                    ],
                            temperature=0.01,
                            max_tokens=max_tokens,
                        )
            ans_1st_pass = response.choices[0].message.content
            break
        except:
            print('retry call gptv', num_trial)
            num_trial += 1
            ans_1st_pass = ''
            time.sleep(10)
    if num_trial == max_num_trial:
        call_api_success = False
    return ans_1st_pass, call_api_success


def check_ocr_box(image_path, display_img = True, output_bb_format='xywh', goal_filtering=None, easyocr_args=None):
    global reader
    if easyocr_args is None:
        easyocr_args = {}
    if reader is None:
        reader = easyocr.Reader(['en']) 
        
    result = reader.readtext(image_path, **easyocr_args)
    is_goal_filtered = False
    if goal_filtering:
        ocr_filter_fs = "Example 1:\n Based on task and ocr results, ```In summary, the task related bboxes are: [([[3060, 111], [3135, 111], [3135, 141], [3060, 141]], 'Share', 0.949013667261589), ([[3068, 197], [3135, 197], [3135, 227], [3068, 227]], 'Link _', 0.3567054243152049), ([[3006, 321], [3178, 321], [3178, 354], [3006, 354]], 'Manage Access', 0.8800734456437066)] ``` \n Example 2:\n Based on task and ocr results, ```In summary, the task related bboxes are: [([[3060, 111], [3135, 111], [3135, 141], [3060, 141]], 'Search Google or type a URL', 0.949013667261589)] ```"
        # message_text = f"Based on the ocr results which contains text+bounding box in a dictionary, please filter it so that it only contains the task related bboxes. The task is: {goal_filtering}, the ocr results are: {str(result)}. Your final answer should be in the exact same format as the ocr results, please do not include any other redundant information, please do not include any analysis."
        message_text = f"Based on the task and ocr results which contains text+bounding box in a dictionary, please filter it so that it only contains the task related bboxes.  Requirement: 1. first give a brief analysis. 2. provide an answer in the format: ```In summary, the task related bboxes are: ..```, you must put it inside ``` ```.  Do not include any info after ```.\n {ocr_filter_fs}\n The task is: {goal_filtering}, the ocr results are: {str(result)}."

        prompt = [{"role":"system", "content": "You are an AI assistant that helps people find the correct way to operate computer or smartphone."}, {"role":"user","content": message_text},]
        print('[Perform OCR filtering by goal] ongoing ...')
        # pred, _, _ = call_gpt4(prompt)
        pred, _, = call_gpt4v(message_text)
        # import pdb; pdb.set_trace()
        try:
            # match = re.search(r"```(.*?)```", pred, re.DOTALL)
            # result = match.group(1).strip()
            # pred = result.split('In summary, the task related bboxes are:')[-1].strip()
            pred = pred.split('In summary, the task related bboxes are:')[-1].strip().strip('```')
            result = ast.literal_eval(pred)
            print('[Perform OCR filtering by goal] success!!! Filtered buttons: ', pred)
            is_goal_filtered = True
        except:
            print('[Perform OCR filtering by goal] failed or unused!!!')
            pass
            # added_prompt = [{"role":"assistant","content":pred},
            #        {"role":"user","content": "given the previous answers, please provide the final answer in the exact same format as the ocr results, please do not include any other redundant information, please do not include any analysis."}]
            # prompt.extend(added_prompt)
            # pred, _, _ = call_gpt4(prompt)
            # print('goal filtering pred 2nd:', pred)
            # result = ast.literal_eval(pred)
    # print('goal filtering pred:', result[-5:])
    coord = [item[0] for item in result]
    text = [item[1] for item in result]
    # confidence = [item[2] for item in result]
    # if confidence_filtering:
    #     coord = [coord[i] for i in range(len(coord)) if confidence[i] > confidence_filtering]
    #     text = [text[i] for i in range(len(text)) if confidence[i] > confidence_filtering]
    # read the image using cv2
    if display_img:
        opencv_img = cv2.imread(image_path)
        opencv_img = cv2.cvtColor(opencv_img, cv2.COLOR_RGB2BGR)
        bb = []
        for item in coord:
            x, y, a, b = get_xywh(item)
            # print(x, y, a, b)
            bb.append((x, y, a, b))
            cv2.rectangle(opencv_img, (x, y), (x+a, y+b), (0, 255, 0), 2)
        
        # Display the image
        plt.imshow(opencv_img)
    else:
        if output_bb_format == 'xywh':
            bb = [get_xywh(item) for item in coord]
        elif output_bb_format == 'xyxy':
            bb = [get_xyxy(item) for item in coord]
        # print('bounding box!!!', bb)
    return (text, bb), is_goal_filtered


def get_phi3v_model_dict():
    from PIL import Image 
    import requests 
    from transformers import AutoModelForCausalLM 
    from transformers import AutoProcessor 

    model_id = "microsoft/Phi-3-vision-128k-instruct" 
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map="cuda", trust_remote_code=True, torch_dtype="auto")
    processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True) 
    print('phi3v model loaded!!!')
    return {'model': model, 'processor': processor}


def call_phi3v(messages, image_base64, model_dict):
    model, processor = model_dict['model'], model_dict['processor']
    device = model.device

    prompt = processor.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    image = Image.open(io.BytesIO(base64.b64decode(image_base64)))
    inputs = processor(prompt, [image], return_tensors="pt").to(device) 

    generation_args = { 
        "max_new_tokens": 1024, 
        "temperature": 0.9, 
        "do_sample": False, 
    } 
    
    generate_ids = model.generate(**inputs, eos_token_id=processor.tokenizer.eos_token_id, **generation_args) 
    # remove input tokens 
    generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]
    ans = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0] 
    return ans

def get_pred_phi3v(prompt_origin, image_base64, label_coordinates, summarize_history=True, verbose=True, history=None, id_key='Click ID', model_dict=None):
    
    single_call = True
    message_text, goal = prompt_origin
    if single_call: 
        messages = [ 
            {"role": "user", "content": '<|image_1|>\n' + message_text} 
        ] 
        ans = call_phi3v(messages, image_base64, model_dict)
        print('phi3v ans:', ans)
    else:
        messages = [ 
            {"role": "user", "content": f'<|image_1|>\n Please give a detailed description of the screenshot image.'} 
        ] 
        ans_1st_pass = call_phi3v(messages, image_base64, model_dict)

        messages.extend([ 
            {"role": "assistant", "content": ans_1st_pass},
            {"role": "user", "content": message_text}
        ])
        ans = call_phi3v(messages, image_base64, model_dict)

    try: 
        match = re.search(r"```(.*?)```", ans, re.DOTALL)
        if match:
            result = match.group(1).strip()
            pred = result.split('In summary, the next action I will perform is:')[-1].strip().replace('\\', '')
            pred = ast.literal_eval(pred)
        else:
            pred = ans.split('In summary, the next action I will perform is:')[-1].strip().replace('\\', '')
            pred = ast.literal_eval(pred)

        if pred[id_key]:
            icon_id = pred[id_key]
            bbox = label_coordinates[str(icon_id)]
            pred['click_point'] = [bbox[0] + bbox[2]//2, bbox[1] + bbox[3]//2]
    except:
        print('gptv action regex extract fail!!!')
        pred = {'action_type': 'CLICK', 'click_point': [0, 0], 'value': 'None', 'is_completed': False}

    step_pred_summary = None
    if summarize_history:
        step_pred_summary, _ = call_gpt4v_new('Summarize what action you decide to perform in the current step, in one sentence, and do not include any icon box number: ' + ans)
        # print('step_pred_summary', step_pred_summary)
    return pred, [True, ans, None, step_pred_summary]


from typing import List, Optional, Union, Tuple

import cv2
import numpy as np

from supervision.detection.core import Detections
from supervision.draw.color import Color, ColorPalette


class BoxAnnotator:
    """
    A class for drawing bounding boxes on an image using detections provided.

    Attributes:
        color (Union[Color, ColorPalette]): The color to draw the bounding box,
            can be a single color or a color palette
        thickness (int): The thickness of the bounding box lines, default is 2
        text_color (Color): The color of the text on the bounding box, default is white
        text_scale (float): The scale of the text on the bounding box, default is 0.5
        text_thickness (int): The thickness of the text on the bounding box,
            default is 1
        text_padding (int): The padding around the text on the bounding box,
            default is 5

    """

    def __init__(
        self,
        color: Union[Color, ColorPalette] = ColorPalette.DEFAULT,
        thickness: int = 3, # 1 for seeclick 2 for mind2web and 3 for demo
        text_color: Color = Color.BLACK,
        text_scale: float = 0.5, # 0.8 for mobile/web, 0.3 for desktop # 0.4 for mind2web
        text_thickness: int = 2, #1, # 2 for demo
        text_padding: int = 10,
        avoid_overlap: bool = True,
    ):
        self.color: Union[Color, ColorPalette] = color
        self.thickness: int = thickness
        self.text_color: Color = text_color
        self.text_scale: float = text_scale
        self.text_thickness: int = text_thickness
        self.text_padding: int = text_padding
        self.avoid_overlap: bool = avoid_overlap

    def annotate(
        self,
        scene: np.ndarray,
        detections: Detections,
        labels: Optional[List[str]] = None,
        skip_label: bool = False,
        image_size: Optional[Tuple[int, int]] = None,
    ) -> np.ndarray:
        """
        Draws bounding boxes on the frame using the detections provided.

        Args:
            scene (np.ndarray): The image on which the bounding boxes will be drawn
            detections (Detections): The detections for which the
                bounding boxes will be drawn
            labels (Optional[List[str]]): An optional list of labels
                corresponding to each detection. If `labels` are not provided,
                corresponding `class_id` will be used as label.
            skip_label (bool): Is set to `True`, skips bounding box label annotation.
        Returns:
            np.ndarray: The image with the bounding boxes drawn on it

        Example:
            ```python
            import supervision as sv

            classes = ['person', ...]
            image = ...
            detections = sv.Detections(...)

            box_annotator = sv.BoxAnnotator()
            labels = [
                f"{classes[class_id]} {confidence:0.2f}"
                for _, _, confidence, class_id, _ in detections
            ]
            annotated_frame = box_annotator.annotate(
                scene=image.copy(),
                detections=detections,
                labels=labels
            )
            ```
        """
        font = cv2.FONT_HERSHEY_SIMPLEX
        for i in range(len(detections)):
            x1, y1, x2, y2 = detections.xyxy[i].astype(int)
            class_id = (
                detections.class_id[i] if detections.class_id is not None else None
            )
            idx = class_id if class_id is not None else i
            color = (
                self.color.by_idx(idx)
                if isinstance(self.color, ColorPalette)
                else self.color
            )
            cv2.rectangle(
                img=scene,
                pt1=(x1, y1),
                pt2=(x2, y2),
                color=color.as_bgr(),
                thickness=self.thickness,
            )
            if skip_label:
                continue

            text = (
                f"{class_id}"
                if (labels is None or len(detections) != len(labels))
                else labels[i]
            )

            text_width, text_height = cv2.getTextSize(
                text=text,
                fontFace=font,
                fontScale=self.text_scale,
                thickness=self.text_thickness,
            )[0]

            if not self.avoid_overlap:
                text_x = x1 + self.text_padding
                text_y = y1 - self.text_padding

                text_background_x1 = x1
                text_background_y1 = y1 - 2 * self.text_padding - text_height

                text_background_x2 = x1 + 2 * self.text_padding + text_width
                text_background_y2 = y1
                # text_x = x1 - self.text_padding - text_width
                # text_y = y1 + self.text_padding + text_height
                # text_background_x1 = x1 - 2 * self.text_padding - text_width
                # text_background_y1 = y1
                # text_background_x2 = x1
                # text_background_y2 = y1 + 2 * self.text_padding + text_height
            else:
                text_x, text_y, text_background_x1, text_background_y1, text_background_x2, text_background_y2 = get_optimal_label_pos(self.text_padding, text_width, text_height, x1, y1, x2, y2, detections, image_size)

            cv2.rectangle(
                img=scene,
                pt1=(text_background_x1, text_background_y1),
                pt2=(text_background_x2, text_background_y2),
                color=color.as_bgr(),
                thickness=cv2.FILLED,
            )
            # import pdb; pdb.set_trace()
            box_color = color.as_rgb()
            luminance = 0.299 * box_color[0] + 0.587 * box_color[1] + 0.114 * box_color[2]
            text_color = (0,0,0) if luminance > 160 else (255,255,255)
            cv2.putText(
                img=scene,
                text=text,
                org=(text_x, text_y),
                fontFace=font,
                fontScale=self.text_scale,
                # color=self.text_color.as_rgb(),
                color=text_color,
                thickness=self.text_thickness,
                lineType=cv2.LINE_AA,
            )
        return scene
    

def box_area(box):
        return (box[2] - box[0]) * (box[3] - box[1])

def intersection_area(box1, box2):
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    return max(0, x2 - x1) * max(0, y2 - y1)

def IoU(box1, box2, return_max=True):
    intersection = intersection_area(box1, box2)
    union = box_area(box1) + box_area(box2) - intersection
    if box_area(box1) > 0 and box_area(box2) > 0:
        ratio1 = intersection / box_area(box1)
        ratio2 = intersection / box_area(box2)
    else:
        ratio1, ratio2 = 0, 0
    if return_max:
        return max(intersection / union, ratio1, ratio2)
    else:
        return intersection / union


def get_optimal_label_pos(text_padding, text_width, text_height, x1, y1, x2, y2, detections, image_size):
    """ check overlap of text and background detection box, and get_optimal_label_pos, 
        pos: str, position of the text, must be one of 'top left', 'top right', 'outer left', 'outer right' TODO: if all are overlapping, return the last one, i.e. outer right
        Threshold: default to 0.3
    """

    def get_is_overlap(detections, text_background_x1, text_background_y1, text_background_x2, text_background_y2, image_size):
        is_overlap = False
        for i in range(len(detections)):
            detection = detections.xyxy[i].astype(int)
            if IoU([text_background_x1, text_background_y1, text_background_x2, text_background_y2], detection) > 0.3:
                is_overlap = True
                break
        # check if the text is out of the image
        if text_background_x1 < 0 or text_background_x2 > image_size[0] or text_background_y1 < 0 or text_background_y2 > image_size[1]:
            is_overlap = True
        return is_overlap
    
    # if pos == 'top left':
    text_x = x1 + text_padding
    text_y = y1 - text_padding

    text_background_x1 = x1
    text_background_y1 = y1 - 2 * text_padding - text_height

    text_background_x2 = x1 + 2 * text_padding + text_width
    text_background_y2 = y1
    is_overlap = get_is_overlap(detections, text_background_x1, text_background_y1, text_background_x2, text_background_y2, image_size)
    if not is_overlap:
        return text_x, text_y, text_background_x1, text_background_y1, text_background_x2, text_background_y2
    
    # elif pos == 'outer left':
    text_x = x1 - text_padding - text_width
    text_y = y1 + text_padding + text_height

    text_background_x1 = x1 - 2 * text_padding - text_width
    text_background_y1 = y1

    text_background_x2 = x1
    text_background_y2 = y1 + 2 * text_padding + text_height
    is_overlap = get_is_overlap(detections, text_background_x1, text_background_y1, text_background_x2, text_background_y2, image_size)
    if not is_overlap:
        return text_x, text_y, text_background_x1, text_background_y1, text_background_x2, text_background_y2
    

    # elif pos == 'outer right':
    text_x = x2 + text_padding
    text_y = y1 + text_padding + text_height

    text_background_x1 = x2
    text_background_y1 = y1

    text_background_x2 = x2 + 2 * text_padding + text_width
    text_background_y2 = y1 + 2 * text_padding + text_height

    is_overlap = get_is_overlap(detections, text_background_x1, text_background_y1, text_background_x2, text_background_y2, image_size)
    if not is_overlap:
        return text_x, text_y, text_background_x1, text_background_y1, text_background_x2, text_background_y2

    # elif pos == 'top right':
    text_x = x2 - text_padding - text_width
    text_y = y1 - text_padding

    text_background_x1 = x2 - 2 * text_padding - text_width
    text_background_y1 = y1 - 2 * text_padding - text_height

    text_background_x2 = x2
    text_background_y2 = y1

    is_overlap = get_is_overlap(detections, text_background_x1, text_background_y1, text_background_x2, text_background_y2, image_size)
    if not is_overlap:
        return text_x, text_y, text_background_x1, text_background_y1, text_background_x2, text_background_y2

    return text_x, text_y, text_background_x1, text_background_y1, text_background_x2, text_background_y2
