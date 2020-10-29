## Writeup

This is standard audio steganography. Although not using common tools or typical LSB coding. Let's start by searching for "audio stego".

Then let's clone and build this tool (it's the fourth result):

- https://github.com/danielcardeenas/AudioStego

Run the tool with the -f option on the audio file and it will display the flag.
The tool uses it's custom audio steg algorithm, and to me it doesn't look like basic LSB, but I may be wrong.

### Flag

> `elite{d1ff3rent_ph4se5_0f_l1f3}`