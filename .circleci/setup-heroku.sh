#!/bin/bash
set -eu

cat > ~/.netrc << EOF
machine api.heroku.com
	login $HEROKU_USERNAME
	password $HEROKU_API_KEY
EOF
chmod 600 ~/.netrc