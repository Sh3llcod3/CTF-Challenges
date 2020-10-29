## Writeup

If you don't know the general premise of what this challenge is about, you will struggle.

Video steg is quite unusual for CTFs, so I thought I'd give it a go. Now you could have something where every other frame or so hides some information and you need to extract it somehow. That's for another challenge.
The way you're supposed to approach this is like any other steg challenge.

> Let's go ahead and run `binwalk -B` on the file first.

__This will yield some weird results__ and will probably throw most people off and lead them down a rabbit hole, but if you extract the PNG image you'll get the first piece of information.
From here, the easiest way is using foremost, but you could theoretically `dd` it with the `skip`/`count` values or even `binwalk` it somehow.

> `foremost Grant_Color.mp4`

This will output two things, the thumbnail (which I thought of hiding something in, except that might be too obvious) or the interesting looking png. Open up the png for the first clue.

> `Password{guitarmass}`

It tells us some sort of password. Note this for later.
The general theme is Video steg. If you google "video steg" then sooner or later you'll come to posts about `TCsteg`.
This is an awesome script mainly written by Martin Fiedler. He has written an in-depth post explaining how it works. Find it [here](https://keyj.emphy.de/real-steganography-with-truecrypt/).

If you follow the reccomendation at the top of the post, you'll need to install [VeraCrypt](https://www.veracrypt.fr/en/Downloads.html). Go ahead and do that for your system or inside a VM.

Then its a simple case of opening `VeraCrypt` and mounting the file as a volume. Use the password from earlier and after a short wait, you will see the file containing the flag.

### Flag

> `ractf{Butt3rsn00k's_R3veng3}`
