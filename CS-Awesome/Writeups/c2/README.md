## Writeup

First we must realise that it's possible to hide zero-width data using unicode steganography. Searching that in google yields this site as the first result:

- https://330k.github.io/misc_tools/unicode_steganography.html

Copy the text and paste it in right box.

Press decode and you get this link:

- https://mega.nz/file/z0kl0BAT#D4381YqPR9F_xEQRLpmHaSlKPvCcAs1g5qaWGz3ZX80

Visit this and you see an image. Download and open it up (the hex). a little way through, you will see an obvious base64 type pattern.


From here, we will need to extract the base64 pattern out of the image file.

- `stat -c %s aerith.jpg` (436676 bytes)

Find the offset we want by looking at it with `xxd`, 133632 bytes roughly.

- `python3 -c "print(436676 - 133632)"`

- `tail -c 303044 aerith.jpg > output.txt`

Open up any text editor and edit out any non-base64 bytes, it starts with `AAAAHGZ0e`.

- `base64 -d output.txt > flag`

- `file flag` (it's ISO Media, Apple iTunes ALAC/AAC-LC so a .m4a file)

> SHA256 of audio file: 5961eb7a2a3640dcb0de520884927647c55972f5941a6b95a0cfc15cf742f197

- `mv flag audio.m4a` (play it)

Listen to what is read out for the flag.

### Flag

`elite{c4tch_m3_if_y0u_c4n}`
