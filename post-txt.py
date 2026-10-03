#!/usr/bin/env python3

import requests
import os
import json
import time

with open(".env") as fp:
    secrets = json.load(fp)

BEARER = secrets["BEARER"]
ZONE_ID = secrets["ZONE_ID"]
DOMAINS = secrets["DOMAINS"]
CERTBOT_VALIDATION = os.environ["CERTBOT_VALIDATION"]
WAIT_TIME = secrets["WAIT_TIME"]

for domain in DOMAINS:
    domain = domain.remove_prefix("*.")
    print("Creating TXT record for _acme-challenge." + domain)

    # Create TXT record for _acme-challenge
    res = requests.post(
        url=f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records",
        headers={
            "Authorization": f"Bearer {BEARER}",
            "Content-Type": "application/json"
        },
        json={
            "type": "TXT",
            "name": f"_acme-challenge.{domain}",
            "content": CERTBOT_VALIDATION,
            "ttl": 120
        }
    )

    if res.status_code != 200:
        print(res.text)
        exit(1)
    else:
        print(f"TXT record created for _acme-challenge.{domain}")

    TXT_RECORD_ID = str(res.json()["result"]["id"])

    with open("/tmp/TXT_RECORD_ID", "a") as fp:
        fp.write(f"{TXT_RECORD_ID},")

    time.sleep(WAIT_TIME)
