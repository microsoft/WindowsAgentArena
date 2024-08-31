#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

source ./shared.sh

mode=azure

# Parse the command line arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --mode)
            mode=$2
            shift 2
            ;;
        --help)
            echo "Usage: $0 [options]"
            echo "Options:"
            echo "  --mode <dev/azure> : Mode (default: azure)"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            log_error_exit "Unknown option: $1"
            ;;
    esac
done

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "$SCRIPT_DIR/../"

# build winarena-base
docker build --build-arg PROFILE_MODE=false -f $SCRIPT_DIR/../src/win-arena-container/Dockerfile-WinArena-Base -t winarena-base:latest $SCRIPT_DIR/../
docker tag winarena-base:latest windowsarena/winarena-base:latest

if [ "$mode" = "dev" ]; then # Only for dev mode
  winarena_image_name="winarena-$mode"
else
  winarena_image_name="winarena"
fi

docker build --build-arg DEPLOY_MODE=$mode -f $SCRIPT_DIR/../src/win-arena-container/Dockerfile-WinArena -t $winarena_image_name:latest $SCRIPT_DIR/../

docker tag $winarena_image_name:latest windowsarena/$winarena_image_name:latest