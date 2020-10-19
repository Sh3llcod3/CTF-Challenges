## Writeup

Let's go straight to the [`email_intercept.txt`](../../Challenges/c1/encrypted_attachment.txt).

Put the first half of the string into an online MD5 lookup tool to get: `bitflip`

Feed https://xor.pw with both the strings (set the correct mode).

This gives us some base64 when output in ascii mode: `bDBOZ19sMXYzX240bk4zUl9tNE4K`

Decode that and we get: `l0Ng_l1v3_n4nN3R_m4N`

According to the email it says to use `Memecrypt`, this can be found [here](https://github.com/Sh3llcod3/Memecrypt).
Pass in the attachment and the decoded string to get the flag.

- `memecrypt -sx -f encrypted_attachment.txt -k l0Ng_l1v3_n4nN3R_m4N`

This is a reference to the YouTube channel [Seannanners](https://www.youtube.com/user/SeaNanners/videos), who had left YouTube previously.

> Since then he has made a [sudden resurgence in 2020](https://youtu.be/LGEtE5ICTIM)

### Flag

`cdctf{r1p_Seanann3r5}`
