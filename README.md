my ssl renewal script

.env file:
```
{
        "BEARER": "xxxxxx",
        "ZONE_ID": "xxxxxx",
        "DOMAINS": ["a4barros.com", "*.a4barros.com", "mail.a4barros.com"],
        "MY_USER": "a4",
        "WAIT_TIME": 120
}
```

The renewal script passes each entry in `DOMAINS` to Certbot as a separate
`-d` argument. `MY_USER` selects the hook script directory under `/home`.
For wildcard entries, the DNS hook creates the TXT record at the base domain's
`_acme-challenge` name.
