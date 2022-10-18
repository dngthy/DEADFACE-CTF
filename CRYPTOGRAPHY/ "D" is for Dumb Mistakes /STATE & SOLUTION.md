To show off their 1337 programming skills, DEADFACE attempted to create their own encryption process to help them communicate privately. Although the encryption process is working, the decryption process is flawed. The De Monne security team was able to find DEADFACE's code and can see that they are trying to use the RSA algorith with these variables:

    Prime numbers of 1049 and 2063
    Exponent of 777887

Recompute the decryption key (d) and submit the flag as flag{d=VALUE}

----------------------------------------------------------------

q = 1049
p = 2063
e = 777887
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
print(d)

>> 1457215

flag{d=1457215}
