#!/bin/bash

# Get the directory of the current script
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

# Path to the JSON configuration file
CONFIG_FILE="$SCRIPT_DIR/../AgentRepoConfig.json"
AGENTS_JSON_FILE="$SCRIPT_DIR/../src/win-arena-container/vm/setup/agents.json"
CLIENT_AGENT_FOLDER="$SCRIPT_DIR/../src/win-arena-container/client/mm_agents"
SERVER_AGENT_FOLDER="$SCRIPT_DIR/../src/win-arena-container/vm/setup/mm_agents"
WIN_STORAGE="$SCRIPT_DIR/../src/win-arena-container/vm/storage"

# Remove the AGENTS_JSON_FILE if it exists
if [ -f "$AGENTS_JSON_FILE" ]; then
    echo "Remove $AGENTS_JSON_FILE."
    rm "$AGENTS_JSON_FILE"
fi

# Remove the WIN_STORAGE if it exists
if [ -d "$WIN_STORAGE" ]; then
    echo "Remove $WIN_STORAGE."
    sudo rm -r $WIN_STORAGE
fi

# Check if jq is installed
if ! command -v jq &> /dev/null
then
    echo "jq could not be found, installing jq..."
    sudo apt-get update && sudo apt-get install -y jq
fi

# Initialize an empty array to hold server repositories
server_repos=()

# Read the JSON file and clone the repositories
repos=$(jq -c '.repositories[]' "$CONFIG_FILE")
for repo in $repos; do
    REPO_DIR_NAME=$(echo "$repo" | jq -r '.name')
    RUNNING_MODE=$(echo "$repo" | jq -r '.runningmode')

    # Set the target folder based on the running mode
    if [ "$RUNNING_MODE" == "client" ]; then
        TARGET_FOLDER="$CLIENT_AGENT_FOLDER"
    elif [ "$RUNNING_MODE" == "server" ]; then
        TARGET_FOLDER="$SERVER_AGENT_FOLDER"
        server_repos+=("$repo")
    else
        echo "Invalid running mode: $RUNNING_MODE"
        exit 1
    fi

    REPO_DIR="$TARGET_FOLDER/$REPO_DIR_NAME"

    if [ -d "$REPO_DIR" ]; then
        echo "Remove $REPO_DIR."
        # Remove the repository directory
        sudo rm -r $REPO_DIR
    fi
done