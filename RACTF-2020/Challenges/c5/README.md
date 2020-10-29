## Briefing

Get your forensics gloves out.

We've managed to exploit a network service running on a C2 server used for orchestrating a large botnet. From there we were able to escalate our privileges and use that server as a proxy to pivot to other machines in the network.

It's quite fascinating, based on the machines we have found, we think that these guys are a known bad actor, responsible for leaking private documents and data from corporate and government targets, which changes our current focus from a reconnaissance mission to a criminal investigation which involves gathering evidence on them so we can attribute names to actions for further prosecution in the courts.

Thus, we've started to image the disks of all the machines we have managed to pivot on. It's not the most ideal circumstances for admissibility of evidence, but we do have a warrant on the guys involved and we can let our lawyers do the rest. Anyway, I've attached a disk image of a small Linux server which we believe they're using for temporarily keeping exfiltrated files.

Can you take a look and see what you find?

### Files Required

[`files.zip`](files.zip) has been zipped with a password of `linux`.