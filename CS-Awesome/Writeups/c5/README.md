## Writeup

This one is somewhat tricky but not too much given a bit of packet crafting knowledge.

This uses the covert_tcp tool to hide a byte per packet in the `IP ID` header field.
So that's what's used here, except the data is encoded with base85.

Thus, each packet needs one byte extracted from that header field. Once done, base85 decode it. and you will have the flag.

### Flag

> `elite{sl1c3_m3_up_r3al_g0Od}`