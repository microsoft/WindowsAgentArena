import os
import argparse
import json

def get_result(target_dir):
    if not os.path.exists(target_dir):
        print("New experiment, no result yet.")
        return None
    
    all_result = []
    domain_result = {}
    all_result_for_analysis = {}
    missing_domains = {}

    for domain in os.listdir(target_dir):
        domain_path = os.path.join(target_dir, domain)
        if os.path.isdir(domain_path):
            for example_id in os.listdir(domain_path):
                example_path = os.path.join(domain_path, example_id)
                if os.path.isdir(example_path):
                    if "result.txt" in os.listdir(example_path):
                        # empty all files under example_id
                        if domain not in domain_result:
                            domain_result[domain] = []
                        result = open(os.path.join(example_path, "result.txt"), "r").read()
                        try:
                            domain_result[domain].append(float(result))
                        except:
                            domain_result[domain].append(float(bool(result)))

                        if domain not in all_result_for_analysis:
                            all_result_for_analysis[domain] = {}
                        all_result_for_analysis[domain][example_id] = domain_result[domain][-1]

                        try:
                            result = open(os.path.join(example_path, "result.txt"), "r").read()
                            try:
                                all_result.append(float(result))
                            except:
                                all_result.append(float(bool(result)))
                        except:
                            all_result.append(0.0)
                    else:
                        print("No result.txt in", example_path)
                        if domain not in missing_domains:
                            missing_domains[domain] = []
                        missing_domains[domain].append(example_id)

    for domain in domain_result:
        print("Domain:", domain, "Executed tasks:", len(domain_result[domain]), "Success Rate:",
              sum(domain_result[domain]) / len(domain_result[domain]) * 100, "%")

    print(">>>>>>>>>>>>>")
    office_success_rate = sum(
        domain_result.get("libreoffice_calc", []) + domain_result.get("libreoffice_impress", []) + domain_result.get(
            "libreoffice_writer", [])) / len(
        domain_result.get("libreoffice_calc", []) + domain_result.get("libreoffice_impress", []) + domain_result.get(
            "libreoffice_writer", [])) * 100
    if office_success_rate:
        print("Office", "Success Rate:", office_success_rate, "%")
    print("Daily", "Success Rate:",
          sum(domain_result.get("vlc", []) + domain_result.get("thunderbird", []) + domain_result.get("chrome", [])) / len(
              domain_result.get("vlc", []) + domain_result.get("thunderbird", []) + domain_result.get("chrome", [])) * 100, "%")
    professional_results = domain_result.get("gimp", []) + domain_result.get("vs_code", [])
    if professional_results:
        print("Professional", "Success Rate:", sum(professional_results) / len(professional_results) * 100, "%")
    else:
        print("Professional", "Success Rate: No data available")

    with open(os.path.join(target_dir, "all_result.json"), "w") as f:
        json.dump(all_result_for_analysis, f, indent=4)
    with open(os.path.join(target_dir, "missing.json"), "w") as f:
        json.dump(missing_domains, f, indent=4)

    if not all_result:
        print("New experiment, no result yet.")
        return None
    else:
        print("Tasks executed:", len(all_result), "Current Success Rate:", sum(all_result) / len(all_result) * 100, "%")
        return all_result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run end-to-end evaluation on the benchmark")
    parser.add_argument("--action_space", type=str, default="pyautogui", help="Action type")
    parser.add_argument("--use_model", type=str, default="gpt-4o", help="Model type") #gpt-4o-mini or gpt-4-vision-preview or gpt-4o or gpt-4-1106-vision-preview
    parser.add_argument("--observation_type", type=str, default="a11y_tree", help="Observation type")
    parser.add_argument("--result_dir", type=str, default="./results", help="Result directory")
    parser.add_argument("--trial_id", type=int, default=0, help="Trial ID")
    args = parser.parse_args()

    target_dir = os.path.join(args.result_dir, args.action_space, args.observation_type, args.use_model, str(args.trial_id))

    get_result(target_dir)

        