## Writeup

In terms of forensics, you can install FTK Imager (Windows) or Autopsy but given that this image contains no system binaries and is a relatively clean and safe image, it's probably ok to just mount the ISO and go through it with a file manager. Right, so let's do just that, let's start by mounting the image, literally right click works here.

Now, let's cd to it and see what it contains:

```shell
$ ls

bin  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

It's a typical FHS system. Let's look under `/home` and `/root` because that's typically where user files are kept.

```shell
$ ls home/ root/
home/:
nothingh.asc  track2.m4a  track.m4a

root/:
private.pgp  public.pgp
```

The tracks are nothing, they're nice tunes though. But we do have a public/private PGP key pair and an interesting file called 'nothingh.asc'
Now clearly, it's pretty obvious that the file is GPG encrypted, let's pop a VM or a docker container to import the keys and decrypt the file. This helps to not clobber the GPG keyring of the host system which is real nice, since I don't like to import GPG keys willy-nilly. I'm going to use an alpine docker container here, but you can use any Kali or throwaway VM:

```shell
$ docker pull alpine
Using default tag: latest
latest: Pulling from library/alpine
cbdbe7a5bc2a: Pull complete
Digest: sha256:9a839e63dad54c3a6d1834e29692c8492d93f90c59c978c1ed79109ea4fb9a54
Status: Downloaded newer image for alpine:latest
docker.io/library/alpine:latest

$ docker run -it alpine

/ # apk update
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
v3.11.6-10-g3d1aef7a83 [http://dl-cdn.alpinelinux.org/alpine/v3.11/main]
v3.11.6-13-g5da24b5794 [http://dl-cdn.alpinelinux.org/alpine/v3.11/community]
OK: 11270 distinct packages available

/ # apk upgrade
OK: 6 MiB in 14 packages

/ # apk add gnupg
(1/28) Installing libgpg-error (1.36-r2)
(2/28) Installing libassuan (2.5.3-r0)
(3/28) Installing libcap (2.27-r0)
(4/28) Installing libffi (3.2.1-r6)
(5/28) Installing libintl (0.20.1-r2)
(6/28) Installing libblkid (2.34-r1)
(7/28) Installing libmount (2.34-r1)
(8/28) Installing pcre (8.43-r0)
(9/28) Installing glib (2.62.6-r0)
(10/28) Installing ncurses-terminfo-base (6.1_p20200118-r4)
(11/28) Installing ncurses-libs (6.1_p20200118-r4)
(12/28) Installing libgcrypt (1.8.5-r0)
(13/28) Installing libsecret (0.19.1-r0)
(14/28) Installing pinentry (1.1.0-r2)
Executing pinentry-1.1.0-r2.post-install
(15/28) Installing libbz2 (1.0.8-r1)
(16/28) Installing gmp (6.1.2-r1)
(17/28) Installing nettle (3.5.1-r0)
(18/28) Installing p11-kit (0.23.18.1-r0)
(19/28) Installing libtasn1 (4.15.0-r0)
(20/28) Installing libunistring (0.9.10-r0)
(21/28) Installing gnutls (3.6.10-r1)
(22/28) Installing libksba (1.3.5-r0)
(23/28) Installing db (5.3.28-r1)
(24/28) Installing libsasl (2.1.27-r5)
(25/28) Installing libldap (2.4.48-r1)
(26/28) Installing npth (1.6-r0)
(27/28) Installing sqlite-libs (3.30.1-r1)
(28/28) Installing gnupg (2.2.19-r0)
Executing busybox-1.31.1-r9.trigger
OK: 25 MiB in 42 packages
/ #
```

> Now open a new terminal tab and leave container running

```shell
$ docker cp home/nothingh.asc container_name:/root
$ docker cp root/private.pgp container_name:/root
$ docker cp root/public.pgp container_name:/root
```

> Close tab and switch back to container

```shell
/ # cd
~ # ls
nothingh.asc  private.pgp   public.pgp

~ # gpg --import private.pgp
gpg: directory '/root/.gnupg' created
gpg: keybox '/root/.gnupg/pubring.kbx' created
gpg: /root/.gnupg/trustdb.gpg: trustdb created
gpg: key 10F3E6C8D8DD2E97: public key "Cloud Strife (Was never in doubt!) <cloud@avalanche-midgar.org>" imported
gpg: key 10F3E6C8D8DD2E97: secret key imported
gpg: Total number processed: 1
gpg:               imported: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1
~ # gpg --import public.pgp
gpg: key 10F3E6C8D8DD2E97: "Cloud Strife (Was never in doubt!) <cloud@avalanche-midgar.org>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1

~ # gpg --decrypt nothingh.asc > nothinghere.txt
gpg: error getting version from 'scdaemon': No SmartCard daemon
gpg: anonymous recipient; trying secret key AFC81B19C65AE957 ...
gpg: okay, we are the anonymous recipient.
gpg: encrypted with RSA key, ID 0000000000000000

~ # apk add file
(1/2) Installing libmagic (5.37-r1)
(2/2) Installing file (5.37-r1)
Executing busybox-1.31.1-r9.trigger
OK: 31 MiB in 44 packages

~ # file nothinghere.txt
nothinghere.txt: HTML document, ASCII text, with very long lines

~ # mv nothinghere.txt nothinghere.html

~ # readlink -f nothinghere.html
/root/nothinghere.html
```

> Open a new tab again and copy it over to host, I am aware this is long winded but I like the isolation

```shell
$ docker cp container_name:/root/nothinghere.html ~/
```

Now delete the container and open the file in browser:
```shell
~ # exit
$ docker rm container_name
```

Now, open the `nothinghere.html` in your browser and you'll see an ASCII art image of [Tifa Lockhart](https://en.wikipedia.org/wiki/Tifa_Lockhart)
The important thing here is that, the ascii art is made of hex characters, so let's copy that, decode it and send it to a file.

I'll be using python but literally anything works here.

> Copy the part from `89504e470d0a1a....all the way to....454e44ae426082` [The 0s on the end are irrelevant]

```shell
~$ python3
Python 3.8.2 (default, Apr 27 2020, 15:53:34)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
```
```python
>>> a = """
...
... 89504e470d0a .......(all the way to the end).......49454e44ae426082"""

>>> import binascii

>>> output = binascii.unhexlify(a.replace('\n','').strip().encode()) # Remember to strip stray spaces and newlines!

>>> with open("output","wb") as something:
...     something.write(output)
...
8060

>>> exit
```
```shell
$ file output
output: PNG image data, 1162 x 86, 8-bit grayscale, non-interlaced

$ mv output output.png
```

Now open the file using your favourite file manager. It's an image containing the flag.

### Flag

> `ractf{b4s1c_d1sk_f0r3ns1cs}`
