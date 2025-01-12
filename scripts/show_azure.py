import os
import json
import logging
import numpy as np
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from io import StringIO

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Validate the experiment configuration
def validate_config(config):
    required_keys = ["exp_name", "a11y_backend", "som_origin", "model_name"]
    for exp_name, exp_details in config.items():
        for key in required_keys:
            if key not in exp_details:
                raise ValueError(f"Missing '{key}' in experiment '{exp_name}'")

# Process each experiment and gather results
def process_experiment(exp_name, exp_details, result_dir, columns):
    row = {col: None for col in columns}
    row["exp_name"] = exp_name
    row["uia_value"] = "✅" if exp_details.get("a11y_backend", "") == "uia" else "❌"
    row["som_origin"] = exp_details.get("som_origin", "N/A")
    row["model"] = exp_details.get("model_name", "Unknown")

    path_kwargs = {
        "result_dir": result_dir,
        "exp_name": exp_name,
        "action_space": "pyautogui",
        "observation_type": "a11y_tree",
        "model": exp_details["model_name"],
        "trial_id": "0"
    }

    path_args = [path_kwargs[k] for k in [
        "result_dir", "exp_name", "action_space", "observation_type", "model", "trial_id"
    ]]
    
    results_path = os.path.join(*path_args)
    errs = 0

    for domain in ["chrome", "libreoffice_calc", "libreoffice_writer", 
                   "vlc", "vs_code", "settings", "windows_calc", 
                   "clock", "msedge", "file_explorer", "microsoft_paint", "notepad"]:
        domain_path = os.path.join(results_path, domain)
        if os.path.isdir(domain_path):
            task_results = []
            for task in os.listdir(domain_path):
                task_path = os.path.join(domain_path, task, "result.txt")
                if os.path.isfile(task_path):
                    try:
                        with open(task_path, "r") as f:
                            result = float(f.read().strip())
                        task_results.append(result)
                    except ValueError:
                        logging.error(f"Invalid result.txt in {exp_name}, {domain}/{task}")
                        errs += 1
                        task_results.append(np.nan)
                else:
                    logging.warning(f"Missing result.txt in {exp_name}, {domain}/{task}")
                    errs += 1
                    task_results.append(np.nan)

            # Calculate the percentage of valid results
            if task_results:
                valid_results = [res for res in task_results if not np.isnan(res)]
                row[domain] = sum(valid_results) / len(valid_results) * 100 if valid_results else None
            else:
                row[domain] = None
        else:
            row[domain] = None

    row["*errors*"] = errs
    return row

# Main function to generate results table from experiments
def get_results_from_json(result_dir, config, output_file):
    columns = ["exp_name", "uia_value", "som_origin", "model",
               "chrome", "libreoffice_calc", "libreoffice_writer", 
               "vlc", "vs_code", "settings", "windows_calc", 
               "clock", "msedge", "file_explorer", "microsoft_paint", "notepad", "*errors*"]
    
    # Prepare markdown headers
    output = StringIO()
    output.write("| " + " | ".join(columns) + " |\n")
    output.write("|" + " | ".join(["---"] * len(columns)) + "|\n")

    # Process each experiment in parallel
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda exp: process_experiment(exp[0], exp[1], result_dir, columns), config.items()))

    # Write results to output file in one go
    for row in results:
        row_markdown = "| " + " | ".join([str(row[col]) if row[col] is not None else "" for col in columns]) + " |\n"
        output.write(row_markdown)

    with open(output_file, "w") as f:
        f.write(output.getvalue())

    logging.info(f"Results table saved to {output_file}")

if __name__ == "__main__":
    import argparse

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate results table from JSON config.")
    parser.add_argument("--result_dir", type=str, required=True, help="Directory containing result files.")
    parser.add_argument("--json_config", type=str, required=True, help="Path to JSON config file.")
    parser.add_argument("--output_file", type=str, default="results_table.md", help="Output markdown file.")

    # Parse arguments
    args = parser.parse_args()

    # Load the JSON configuration
    with open(args.json_config, "r") as f:
        config = json.load(f)

    # Validate the configuration
    try:
        validate_config(config)
    except ValueError as e:
        logging.error(f"Configuration error: {e}")
        exit(1)

    # Process and generate the results table
    get_results_from_json(args.result_dir, config, args.output_file)
