Now that you know the correct RSA decryption value d from "D" is for Dumb Mistakes, can you use it to properly decrypt one of DEADFACE's private messages? The ciphertext that De Monne's security team intercepted was:

992478-1726930-1622358-1635603-1385290

Assuming each - character separates each letter of the ciphertext and every letter in the alphabet is represented by its position (i.e., a = 1, b = 2, etc.), what is the plaintext version of this message? Submit the flag as flag{plaintext}.

----------------------------------------------------------------

q = 1049
p = 2063
e = 777887
n = qp = 2164087
phi = (p-1)*(q-1) = 2160976
d = 1457215
cipher ="992478-1726930-1622358-1635603-1385290"

Split cipher text into arrays:
letters = ["992478", "1726930", "1622358", "1635603", "1385290"]

Using https://www.dcode.fr/rsa-cipher to decrypt each element of letters array.
Select display mode: Plaintext as Integer number
Combine integer values into arrays:

Script:
decrypt_code = [7, 8, 15, 19, 20]
plaintext = ""
for i in decrypt_code:
    plaintext += chr(i+96)
print(plaintext)

>> ghost
flag{ghost}
