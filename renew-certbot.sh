#!/bin/sh

certbot certonly --manual --preferred-challenges dns-01 -d "a4mail.a4barros.com" --manual-auth-hook "python3 /home/a4/certbot-renew/post-txt.py" --manual-cleanup-hook "python3 /home/a4/certbot-renew/delete-txt.py"
