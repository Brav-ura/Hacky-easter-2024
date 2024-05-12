# Description
This time, Bunny Bob was lost in thoughts. _"I cracked your code"_, the young bunny from before told him. _"Is this using the same number again? It's irrational to think this would work twice."_

_"No"_, Bob replied. _"It's not that irrational at all, when you have a closer look."_

_"But my approach doesn't work here at all!"_ Bunny Bob sighed.

_"It's the same mechanic. Just don't start at the beginning. Start right after every hacker's birthday."_

His young friend looked at him quizzically and hopped away, none the wiser.

Here's the encoded flag:

```
he876:|I94kcxk6uohyp9t4cn}ti:vtcir7foowg8tbk8sfy~4166~  
```

## Hint
It's not 𝛑 this time.
# Solution
After plenty of time reading about different irrational numbers, like e, the golden ratio, square root of 3 and 9, the wiki page on Euler's constant (e) https://en.wikipedia.org/wiki/Euler's_constant and https://encyclopediaofmath.org/wiki/Euler_constant, it's irrationality is put into question since it can be represented as a continued fraction that is known to have at least 475,006 terms, potentially infinite if e is indeed irrational.

![euler](../Screenshots/Pasted%20image%2020240509222203.png)

Going from this, if e is the constant we've got to use, the next thing is get as many digits as we can, since every hacker's birthday didn't ring a bell, and trying to search for it lead nowhere.

Searching for `digits of constant e download` led to this page https://archive.org/details/EulersNumberE7.5BillionDigits where there are 7.5 billion digits of e. Surely that's enough, right?

To download the file I curl it and save the output into a file with `curl https://archive.org/download/EulersNumberE7.5BillionDigits/part1.txt -o part1.txt`

One thing to take into account is that the first 7 digits to ROT can be known, since the flag will start with `he2024{`.

Doing the rotations manually, with ROT47 in cyberchef and negative numbers due to the way our previously implementation worked, reveals that the first numbers are 0067461, as doing that many rotations will make the encoded flag characters be `he2024{`.

If the mechanism is the same as in Piece of Cake 1, let's modify the previous script to go over the digits on the file and attempt to do the rotations.

Our script will open one of the files with the digits of *e*, in 54 byte chunks, have a function for the ROT, and keep looking until it reads all the file.

Since it's possible for the same sequence to be several times on the file, it will only print the rotation for those that not only have those digits, but if the last character is a closing angle bracket.

```
import time
encoded_flag = "he876:|I94kcxk6uohyp9t4cn}ti:vtcir7foowg8tbk8sfy~4166~"#54 digits are needed

def rot(letter, number):
    #turn letter to ascii decimal value
    letter = ord(letter)
    #substracting the ascii decimal value a number of times will rotate it by that much
    rotated = letter - int(number)
    return chr(rotated)

flag = ''
file_name = 'E:\\digits_e\\part1.txt'
offset = 0
buffer_size = 54
expected_initial_digits = "0067461"#taken from manually ROTing the flag to match the characters he2024{
with open(file_name) as f:
    while True:
        f.seek(offset)    
        digits = f.read(buffer_size)
        #if there are no digits then it reached EOF. Also stop reading if there aren't enough digits to do calculation
        if not digits or len(digits) != buffer_size:
            break
        #Only do the ROT if the sequence starts with the pre-calculated numbers
        if digits.startswith(expected_initial_digits):
            for i in enumerate(encoded_flag):
                flag += rot(i[1], digits[i[0]])
            if flag.endswith('}'):
                print("Potential flag: {}\nDigits: {}".format(flag,digits))#The last non printable characters mess up the first d for some reason
                print("Current progress in file: {}%".format((offset / 2000000000) * 100 )) # 2,000,000,000 is the size in bytes of the file. Every character is a byte
        flag = ''
        offset += 1
```

After more than an hour, the following is printed:
```
Potential flag: he2024{C2.i[rh5sf_tk6t1\hxtf5uk]ar1egln`1l_k0n`rx4.01}
Current progress in file: 0.04509135%
Potential flag: he2024{G13c[pc5nkfvh3r3[g{nh6mm\bj6]olse0n]e2lbxy+../}
Digits: 006746128188881742386218726149777819034286566741593871
Current progress in file: 0.75132385%
Potential flag: he2024{G74j\tj4nfcqn5t.`nvne1uo]bk5eokwg2sai2newx0*26}
[SNIPPED]
Potential flag: he2024{G00d_th1ng_th3s3_numb3rs_ar3_not_1mag1nary....}
Digits: 006746129474435789586114087774148047103877147557563881
Current progress in file: 17.659408600000003%
```
So we stop execution now that we have our flag `he2024{G00d_th1ng_th3s3_numb3rs_ar3_not_1mag1nary....}`
