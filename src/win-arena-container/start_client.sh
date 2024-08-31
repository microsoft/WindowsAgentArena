#!/bin/bash

agent="navi"
clean_results=true
worker_id="0"
num_workers="1"
result_dir="./results"
json_name="evaluation_examples_windows/test_all.json"

# parse agent argument
while [[ $# -gt 0 ]]; do
    case "$1" in
        --agent)
            agent=$2
            shift 2
            ;;
        --clean-results)
            clean_results=$2
            shift 2
            ;;
        --worker-id)
            worker_id=$2
            shift 2
            ;;
        --num-workers)
            num_workers=$2
            shift 2
            ;;
        --result-dir)
            result_dir=$2
            shift 2
            ;;
        --json-name)
            json_name=$2
            shift 2
            ;;
        --help)
            echo "Usage: $0 [options]"
            echo "Options:"
            echo "  --agent <agent>          The agent to use (default: navi)"
            echo "  --clean-results <bool>   Clean the results directory before running the client (default: true)"
            echo "  --worker-id <id>         The worker ID"
            echo "  --num-workers <num>      The number of workers"
            echo "  --result-dir <dir>       The directory to store the results (default: ./results)"
            echo "  --json-name <name>       The name of the JSON file to use (default: test_all.json)"
            exit 0
            ;;
        *)
    esac
done

cd /client
if [ "$clean_results" = true ]; then
    echo "Cleaning results directory..."
    rm -rf "$result_dir"/*
fi

echo "Running agent $agent..."
python run.py --agent "$agent" --worker_id "$worker_id" --num_workers "$num_workers" --result_dir "$result_dir" --test_all_meta_path "$json_name"