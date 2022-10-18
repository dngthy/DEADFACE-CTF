ESU's IT staff noticed some peculiar traffic from DEADFACE at the beginning of the attack. They sent a series of handshakes - the IT staff is stumped as to what DEADFACE was trying to do.

What type of scan did DEADFACE launch first?

Submit the flag as flag{scantype}.

Download File
SHA1: c2b1fcb40d8959d24e45752fbb040521c8fcb110
Password: d34df4c3

----------------------------------------------------------------

In pcap file, we see that this is Stealth scan

SYN scan is the default and most popular scan option for good reasons. It can be performed quickly, scanning thousands of ports per second on a fast network not hampered by restrictive firewalls. It is also relatively typical and stealthy since it never completes TCP connections.

The port is also considered open if an SYN packet (without the ACK flag) is received in response.

This technique is often referred to as half-open scanning because you don’t open a full TCP connection. You send an SYN packet as if you are going to open a real connection and then wait for a response. An SYN, ACK indicates the port is listening (open)

flag{stealth}