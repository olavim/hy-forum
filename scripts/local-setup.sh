#!/bin/bash

# Get absolute path to project root
ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/../ >/dev/null 2>&1 && pwd )"

# Run sqitch container with the current and home directories mounted.
docker run -it --rm \
	--mount "type=bind,src=$ROOT/services/backend,dst=/repo" \
	sqitch/sqitch:latest \
	--cd sqitch \
	deploy local
