#reversing #crypto 
# Description
You found this hatch. It should be easy to open, but you might need some force.

## hatchlatch.py
```
from random import *

flag="REDACTED"
cipher=[]
kee=randint(1,10000)
off=randint(1,5)
for f in flag:
    cipher.append(str((ord(f) - off) ^ kee))

# print(cipher)
# ['6255', '6248', '6181', '6183', '6181', '6203', '6258', '6255', '6203', '6267', '6250', '6255', '6230', '6203', '6250', '6250', '6202', '6200', '6200', '6230', '6254', '6245', '6203', '6241', '6267', '6202', '6251', '6256']
```

# Solution
Since we have the source code that creates the cipher, and what seems to be a list with the ciphered text for the flag, we could try to make a code that would decipher the flag.

The things to take note of is that the kee variable is within the range of 1 and 10000, while the off is only from 1 to 5, so those are the numbers that we're going to have to brute force.

Let's make a function that would do the inverse operations from the process that does the cipher.

So `cipher.append(str((ord(f) - off) ^ kee))` would end up as 
```
def decipher(ciphered, kee, off):
    deciphered=[]
    for i in ciphered:
        decrypted = int(i) ^ kee
        decrypted += off
        decrypted_char = chr(decrypted)
        deciphered.append(decrypted_char)
    return deciphered
```

But how to see if our function works? We could try to encrypt a flag that we control with specific values for kee and off. 

By refactoring a bit the ciphering code we end up with:
```
def make_cipher(flag):
    cipher=[]
    #kee=randint(1,10000)
    kee=1337
    #off=randint(1,5)
    off=3
    for f in flag:
        cipher.append(str((ord(f) - off) ^ kee))
    return(cipher)
```

So now the numbers will always be 1337 for kee and 3 for off.
Let's test out our function by ciphering `he2024{test_flag}` and deciphering it
`print(''.join(decipher(make_cipher("he2024{test_flag}"),1337,3)))`
prints back our flag.

Since that works, the last part is to iterate through all of the numbers for when the flag was ciphered

```
for kee in range(1,10000):
    for off in range(1,5):
        flag = ''.join(decipher(cipher_flag, kee, off))
        if 'he2024' in flag:
            print(flag)
```

Running the complete script returns the flag `he2024{h4tch_4cc355_gr4nt3d}`