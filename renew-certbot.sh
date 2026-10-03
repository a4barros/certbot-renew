#!/bin/sh

DOMAIN=$(python3 -c 'import json; print(json.load(open(".env")).get("DOMAIN", ""))')
if [ -z "$DOMAIN" ]; then
	printf '%s\n' "DOMAIN must be set in .env" >&2
	exit 1
fi

certbot certonly --manual --preferred-challenges dns-01 -d "$DOMAIN" --manual-auth-hook "python3 /home/a4/certbot-renew/post-txt.py" --manual-cleanup-hook "python3 /home/a4/certbot-renew/delete-txt.py"
