my ssl renewal script

.env file:
```
{
        "DOMAIN": "a4mail.a4barros.com",
        "MY_USER": "a4",
        "DOMAIN_ID": "xxxxxx",
        "TOKEN": "xxxxxx",
        "WAIT_TIME": 120
}
```

The renewal script uses `DOMAIN` as the domain passed to Certbot.
It uses `MY_USER` to build the paths to the Certbot hook scripts under `/home`.
`DOMAIN` may be a wildcard such as `*.a4barros.com`; the DNS hook creates the
TXT record at `_acme-challenge.a4barros.com` for wildcard validation.
