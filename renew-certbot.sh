#!/bin/sh

DOMAINS=$(python3 -c 'import json; d=json.load(open(".env")).get("DOMAINS", []); print("\n".join(d) if isinstance(d, list) and all(isinstance(x, str) and x for x in d) else "")')
if [ -z "$DOMAINS" ]; then
	printf '%s\n' "DOMAINS must be set in .env" >&2
	exit 1
fi

MY_USER=$(python3 -c 'import json; print(json.load(open(".env")).get("MY_USER", ""))')
if [ -z "$MY_USER" ]; then
	printf '%s\n' "MY_USER must be set in .env" >&2
	exit 1
fi

set --
while IFS= read -r domain; do
	[ -z "$domain" ] || set -- "$@" -d "$domain"
done <<EOF
$DOMAINS
EOF

certbot certonly --manual --preferred-challenges dns-01 "$@" --manual-auth-hook "python3 /home/$MY_USER/certbot-renew/post-txt.py" --manual-cleanup-hook "python3 /home/$MY_USER/certbot-renew/delete-txt.py"
