#!/bin/bash
set -eu

# Install Heroku CLI
wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sudo sh

cat > ~/.netrc << EOF
machine api.heroku.com
	login $HEROKU_USERNAME
	password $HEROKU_API_KEY
EOF
chmod 600 ~/.netrc