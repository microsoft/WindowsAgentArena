#!/bin/bash

# Get the directory of the current script
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

# Path to the JSON configuration file
CONFIG_FILE="$SCRIPT_DIR/../AgentRepoConfig.json"
CLIENT_AGENT_FOLDER="$SCRIPT_DIR/../src/win-arena-container/client/mm_agents"
SERVER_AGENT_FOLDER="$SCRIPT_DIR/../src/win-arena-container/vm/setup/mm_agents"
AGENTS_JSON_FILE="$SCRIPT_DIR/../src/win-arena-container/vm/setup/agents.json"

# Remove the AGENTS_JSON_FILE if it exists
if [ -f "$AGENTS_JSON_FILE" ]; then
    rm "$AGENTS_JSON_FILE"
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
    REPO_URL=$(echo "$repo" | jq -r '.url')
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
        echo "Directory $REPO_DIR already exists. Skipping clone."
    else
        echo "Cloning $REPO_URL into $REPO_DIR..."
        git clone "$REPO_URL" "$REPO_DIR"
    fi
done

# Print the server_repos array
printf '%s\n' "Repo is : ${server_repos[@]}"

# Create the agents.json file with the list of server repositories
jq -n --argjson repos "$(printf '%s\n' "${server_repos[@]}" | jq -s .)" '{"server_repositories": $repos}' > "$AGENTS_JSON_FILE"
