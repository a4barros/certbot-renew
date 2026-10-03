#!/usr/bin/env python3

import requests
import os
import json

with open(".env") as fp:
    secrets = json.load(fp)

BEARER = secrets["BEARER"]
ZONE_ID = secrets["ZONE_ID"]
CERTBOT_VALIDATION = os.environ["CERTBOT_VALIDATION"]
STATE_FILE = "/tmp/certbot_dns_records.json"

if not os.path.exists(STATE_FILE):
    exit(0)

with open(STATE_FILE) as fp:
    records = json.load(fp)

TXT_RECORD_IDS = records.pop(CERTBOT_VALIDATION, [])
for record_id in TXT_RECORD_IDS:
    res = requests.delete(
        url=f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{record_id}",
        headers={
            "Authorization": f"Bearer {BEARER}",
            "Content-Type": "application/json"
        }
    )

    if res.status_code != 200:
        print(res.text)
        exit(1)

if records:
    with open(STATE_FILE, "w") as fp:
        json.dump(records, fp)
else:
    os.remove(STATE_FILE)
