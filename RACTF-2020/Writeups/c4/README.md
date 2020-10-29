## Writeup

This challenge has no logical or coherent solution and I am told this has been responsible for much suffering.
I do apologize for this, I will think several times before creating something like this again.

> Before you read this writeup, I urge you to go check out the excellent writeups from both [`PWN-to-0xE4`](https://github.com/PWN-to-0xE4/Writeups/blob/master/RACTF%202020/Rev%20and%20Pwn/Eccentric%20Encryption%20Enigma.md) and [`TheWinRaRs`](https://github.com/TheWinRaRs/Writeups/blob/master/ractf/pwn/eccentric-encryption-enigma.md).

Anyhow, with the binary, the most obvious thing to do here is to run it.

```shell
$ chmod +x uwu
$ ./uwu
Import error: No module named 'memecrypt', please install this.
E.g. python3 -m pip install <module>

$ python3 -m pip install memecrypt
$ ./uwu
b'H\x91%\xb2]\x9f\x80f\xda\xbf\x8d\x1e\xc8\xb0:\x96\xa2^\xd9\xdb\xad/j\x16p\xce\xb9\xed-\x8a\xb3\xb0'
```

This is where the red herrings start. Those bytes are not important, it's pure random output, trying to comprehend this will waste time.

Let's open it in our favourite BASED debugger `GDB`:

> You don't have to, `radare2` or `IDA` can probably do this quicker.

```shell
$ gdb -q uwu
Reading symbols from uwu...
(gdb) info func
All defined functions:

File ../csu/errno-loc.c:
24:     int *__errno_location(void);

File ../nptl/pthread_mutex_lock.c:
63:     int __pthread_mutex_cond_lock(pthread_mutex_t *);
619:    void __pthread_mutex_cond_lock_adjust(pthread_mutex_t *);
63:     int __pthread_mutex_lock(pthread_mutex_t *);
170:    static int __pthread_mutex_cond_lock_full(pthread_mutex_t *);
...etc........
```

So now from this, list the functions within the binary:

```shell
$ info func (hit enter a few times)
Non-debugging symbols:
0x0000000000401000  _init
0x00000000004011e0  __Pyx_PyErr_GivenExceptionMatches.part.0
0x00000000004012a9  __Pyx__GetException
0x00000000004013fb  __Pyx_copy_spec_to_module
0x0000000000401473  __pyx_pymod_create
0x00000000004015c8  __Pyx__ExceptionReset.isra.0
0x00000000004015fe  __Pyx_Import.constprop.0
0x0000000000401687  __pyx_pymod_exec_owo
0x0000000000405117  PyInit_owo
0x0000000000405123  __Pyx_main.part.0
```

Now the clue here is the '__Pyx_' part. That is how cython converts python functions into C source. So I'm not sure how other debuggers can do this, but with GDB let's try to disassemble some of these functions, using the power of tab completion.

```shell
(gdb) disas __pyx_ (hit tab twice so it autocompletes)
__pyx_bisect_code_objects
__pyx_pw_3owo_11__
__pyx_pw_3owo_13___
__pyx_pw_3owo_15____
__pyx_pw_3owo_17_____
__pyx_pw_3owo_19______
__pyx_pw_3owo_1owo
__pyx_pw_3owo_21_______
__pyx_pw_3owo_23_________
__pyx_pw_3owo_25ractf
__pyx_pw_3owo_27aws_IAM
__pyx_pw_3owo_29serverless_lambda
__pyx_pw_3owo_31i3_tiling_wm
__pyx_pw_3owo_33get_answer
__pyx_pw_3owo_35flag
__pyx_pw_3owo_47main
...and so on........
```

So we have our initial list of functions. There is no clear way to determine which function we might need. Some are just phony functions, others will purposefully try to trick the user, so the only thing to do here is to step through them and see what strings they're loading into memory as well as examine what static strings are there.

These are the functions that have anything to do with the flag:

- `__pyx_pw_3owo_9fbi_man_please_no_...(and so on)...`: The first part of the encrypted flag
- `__pyx_pw_3owo_13___()`: The second part of the flag
- `__pyx_pw_3owo_1owo()`: Last part of secret key
- `__pyx_pw_3owo_31i3_tiling_wm()`: Middle part of key
- `__pyx_pw_3owo_45frag()`: First part of key

What's important is what these functions are loading into memory/strings in stack/heap. So what needs to be done here is the key fragments need to be decrypted and concatenated, then decrypted using memecrypt.
They should be easy to spot since they are small in length and base64 looking, eventually you'll get them:

```shell
$ memecrypt -sx -i QVZHZUEqOnM= -k rain
[+] Decrypted result:
---------------------
frag1

$  memecrypt -sx -i ZGBXYmRbfXU= -k champions
[+] Decrypted result:
---------------------
frag2

$  memecrypt -sx -i T0YqVGBGJzZiLXYp -k apollo
[+] Decrypted result:
---------------------
lastfrag
```

> This makes our key: `frag1frag2lastfrag`

Anyway, now, let's concatenate the flag using the first and second parts. Again, the trick is to spot that
they are base64'd, but only half of the full flag, but examining those functions I mentioned above should get you the encrypted flag:

> `Xjk6Y1N3PDBWdz0jNjlTOFp9bCJ5bWxPRFZuQnxZNFtibWxPWD9udF5tcjgmd1ZbPG1XJw==`

So using that same memecrypt tool, and the key we constructed earlier, let's decrypt this:

```shell
$ memecrypt -sx -i Xjk6Y1N3PDBWdz0jNjlTOFp9bCJ5bWxPRFZuQnxZNFtibWxPWD9udF5tcjgmd1ZbPG1XJw== -k frag1frag2lastfrag
[+] Decrypted result:
---------------------
ractf{Th1ngs_Th4t_I_Cann0t_Compr3hend}
```

There we have it, that's our flag. Now for sake of keeping this writeup compact, I've not going
to include the sneaky tricks here, but there is another fake flag in there too.

### Flag

> `ractf{Th1ngs_Th4t_I_Cann0t_Compr3hend}`
