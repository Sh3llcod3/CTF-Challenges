## Writeup

This is a series of files embedded within each other, with the final step containing an encrypted zip file.

Now you could manually binwalk and extract all the files and binwalk the extracted files till you get to the zip, or as [botters](https://github.com/bottersnike) points out, you can simply just type:

> `binwalk -Me <file>`

Upon doing so, it will recursively extract all files, so let's head to binwalk's output directory, which has a WAV file and an another output directory. Inside is a zip with flag.png, but the zip is password protected.

So let's head back up one more level. Now focusing on the WAV file, when you play it, all you hear is just random noise. That's a big indicator that you need to generate a spectrogram from it.
So let's go ahead and use sox to do just that (ffmpeg/audacity/any audio editing program should work here):

> `sox OwO.wav -n spectrogram`

Open the image and note the password which is `Shad0ws`.
Coming back to the password protected zip file, let's open that with the password. For that using the traditional unzip may not work, so let's use 7zip:

> `7z x <extracted zip>`

Enter our password from earlier and bam! You've got the flag!

### Flag

> `ractf{M0nst3rcat_In5tin3t}`

