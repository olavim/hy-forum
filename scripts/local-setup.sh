#!/bin/bash

# Get absolute path to project root
ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/../ >/dev/null 2>&1 && pwd )"

# Set up required pass-through variables.
user=${USER-$(whoami)}
passopt=(
	-e "SQITCH_ORIG_SYSUSER=$user"
	-e "SQITCH_ORIG_EMAIL=$user@$(hostname)"
	-e "TZ=$(date +%Z)"
	-e "LESS=${LESS:--R}"
)

# Run sqitch container with the current and home directories mounted.
docker run -it --rm --network host \
	-v $ROOT:/app \
	-u $(id -u ${USER}):$(id -g ${USER}) \
	"${passopt[@]}" \
	sqitch/sqitch:latest -C /app/sqitch deploy local

# Rename environment configuration file
cp -n $ROOT/.env.dist $ROOT/.env