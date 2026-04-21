#!/usr/bin/env python3

import requests
import os
import json

with open(".env") as fp:
    secrets = json.load(fp)

BEARER = secrets["BEARER"]
ZONE_ID = secrets["ZONE_ID"]

if not os.path.exists("/tmp/TXT_RECORD_ID"):
    exit(0)

with open("/tmp/TXT_RECORD_ID", mode="r") as fp:
    TXT_RECORD_IDS = fp.read().split(",")

# Normally the certbot puts two TXT records, because we are trying to renew a domain
# and a wildcard domain
for ID in TXT_RECORD_IDS:
    if len(ID) > 1:
        res = requests.delete(
            url=f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{ID}",
            headers={
                "Authorization": f"Bearer {BEARER}",
                "Content-Type": "application/json"
            }
        )

        if res.status_code != 200:
            print(res.text)
            exit(1)

os.remove("/tmp/TXT_RECORD_ID")
