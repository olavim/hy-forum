#!/bin/bash
set -eu

# Install Heroku CLI
wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
sudo mkdir -p /usr/local/lib /usr/local/bin
sudo tar -xvzf heroku-linux-amd64.tar.gz -C /usr/local/lib
sudo ln -s /usr/local/lib/heroku/bin/heroku /usr/local/bin/heroku

cat > ~/.netrc << EOF
machine api.heroku.com
	login $HEROKU_LOGIN
	password $HEROKU_API_KEY
EOF
chmod 600 ~/.netrc