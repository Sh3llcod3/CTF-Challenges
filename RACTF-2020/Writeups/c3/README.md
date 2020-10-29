## Writeup

Once given the capture file, you will need to crack the pre-shared key. This is trivially done with any tool of your choosing, the most common tool used for over a decade is [Aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) or for those who own a compatible GPU, [Hashcat](https://hashcat.net/hashcat/).

The first step is to acquire a decent wordlist. Most wordlists will work here. The infamous `rockyou.txt` immediately springs to mind, and that will work fine for this challenge, but things like `darkc0de.lst` and many others from Daniel Miessler's Seclists will work.

> General purpose wordlists may be in inefficient as WPA2 has a password length requirement of 8-63 characters. Older versions of `aircrack-ng` may have issues with `rockyou.txt`, use `strings rockyou.txt > rockyou_ascii.txt` in that case.

With the tool of your choice, feed in the capture file and wordlist, you'll have the key soon:

> `nighthawk`

Now that we have the PSK, the next step is to decrypt the capture file. Again, you have choice, you could use `airdecap-ng` or `wireshark`.

Let's do it with `wireshark`, they have a good guide [here](https://wiki.wireshark.org/HowToDecrypt802.11).
The key and SSID needs to be specified to wireshark in this format `PSK:SSID` which in our case is:

> `nighthawk:ATLAS_PMC`

Doing that reveals a stream of TCP and HTTP packets, from here opening `File -> Export objects -> HTTP` tells us that there is a PDF, interesting.
Let's export that and save it to disk. Then open the PDF, which is an extract of a financial statement. At the bottom right, you should see your flag.

### Flag

> `ractf{j4ck_ry4n}`

