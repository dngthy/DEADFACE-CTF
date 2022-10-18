Unable to use their RSA encryption program, luciafer resorts to using old school techniques to send a message out to the team. Can you decipher the code and find the flag?

Submit the flag as flag{flag text}

Download Image
SHA1: 1afcf5cc3a64f3924f27425ed344fbe4545c5554

env.deadface.io

----------------------------------------------------------------

This is braille alphabet
We get "PORT⠀#47980"

Access env.deadface.io:47980 , we get "GOBLINS"

Table in the picture describe Vigenere cipher, decipher "DT UFAWDL IQYXFKVL" with:
- key: "GOBLINS"
- alphabet: "ZYXWVUTSRQPONMLKJIHGFEDCBA"
We will get the plain text:
>> WE STRIKE TOMORROW

flag{WE STRIKE TOMORROW}