## Writeup

Steghide is an incredibly common tool that can embed LSB data in some audio and image formats.

so let's go ahead and use steghide to extract the zip.

- `steghide extract -sf Aero_Chord_Take_Me_Home.wav`

> There's no password. You can just press Enter.

From that, we get a `flag.wav` file, just generate a spectrogram of that to get the flag.
I used sox, its fast and versatile.

- `sox flag.wav -n spectrogram`

### Flag

`cdctf{M0n5t3rC4T}`

