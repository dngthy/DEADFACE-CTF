We found this image on Ghost Town. We think bumpyhassan hid some information here. Can you see what information he hid?

SHA1 image: 3b3964ae6751329c221c02cc9303cad3e3472217

----------------------------------------------------------

>> cat doggo.jpg
At the last file we found string: "password:borkbork"

>> steghide --extract -sf doggo.jpg
Enter passphrase: borkbork
wrote extracted data to "itsasecret.pdf"

Open itsasecret.pdf we get the flag:
flag{whos_A_g00d_boi_bork_bork}