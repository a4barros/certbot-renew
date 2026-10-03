my ssl renewal script

.env file:
```
{
        "DOMAIN": "a4mail.a4barros.com",
        "USER": "a4",
        "DOMAIN_ID": "xxxxxx",
        "TOKEN": "xxxxxx",
        "WAIT_TIME": 120
}
```

The renewal script uses `DOMAIN` as the domain passed to Certbot.
It uses `USER` to build the paths to the Certbot hook scripts under `/home`.
