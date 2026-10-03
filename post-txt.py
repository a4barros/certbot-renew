#!/usr/bin/env python3

import requests
import os
import json
import time

with open(".env") as fp:
    secrets = json.load(fp)

BEARER = secrets["BEARER"]
ZONE_ID = secrets["ZONE_ID"]
DOMAIN = os.environ["CERTBOT_DOMAIN"]
if DOMAIN.startswith("*."):
    DOMAIN = DOMAIN[2:]
CERTBOT_VALIDATION = os.environ["CERTBOT_VALIDATION"]
WAIT_TIME = secrets["WAIT_TIME"]

STATE_FILE = "/tmp/certbot_dns_records.json"
print("Creating TXT record for _acme-challenge." + DOMAIN)

res = requests.post(
    url=f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records",
    headers={
        "Authorization": f"Bearer {BEARER}",
        "Content-Type": "application/json"
    },
    json={
        "type": "TXT",
        "name": f"_acme-challenge.{DOMAIN}",
        "content": CERTBOT_VALIDATION,
        "ttl": 120
    }
)

if res.status_code != 200:
    print(res.text)
    exit(1)
print(f"TXT record created for _acme-challenge.{DOMAIN}")

TXT_RECORD_ID = str(res.json()["result"]["id"])
if os.path.exists(STATE_FILE):
    with open(STATE_FILE) as fp:
        records = json.load(fp)
else:
    records = {}
records.setdefault(CERTBOT_VALIDATION, []).append(TXT_RECORD_ID)
with open(STATE_FILE, "w") as fp:
    json.dump(records, fp)

time.sleep(WAIT_TIME)
