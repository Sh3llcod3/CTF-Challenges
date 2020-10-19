## Writeup

This is an old reference, see: https://youtu.be/O3cvmtPuvXo
The hint is also indicative of this.

The pattern in the correct order is:

```
2x 9mm
1x 9mm (Checkbox Selected)
1x .338 (Checkbox Selected)
1x 20mm
1x M16
1x M16 (Checkbox Selected)
1x M134 (Checkbox Selected)
------------------------
Total: $4455
------------------------
```

Hitting checkout with that total in the basket grants a response with the flag.

### Flag

`elite{B1g_Sm0ke's_Ord3r}`

### Setup Required

The assets directory [`server/static.zip`](server/static.zip) has been zipped with a password of `static`.

Ensure that you have docker installed, then deploy the DockerFile and make `main.py` unreadable by the webserver.
The directory path should be `server/static/`. A sha256sum file is included for integrity verification.