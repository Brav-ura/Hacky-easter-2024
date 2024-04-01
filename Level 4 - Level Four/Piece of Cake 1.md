#crypto #misc 
# Description
Bunny Bob grinned from ear to ear, as he told the story of his new idea. "_ROT. It's just ROT. Nothing more. But get this: Each letter is rotted individually, and I am using different numbers for each letter!_".

Fred Rabbit wasn't impressed. "_Hmm. Interesting. How do you communicate the needed individual rotations to the recipient?_".  
"_Oh. That_", Bob smiled. "_You could say it's a piece of cake._"

Here's the encoded flag:

```
ii35;6Ykf|h~j8adgf7ve5uuiw37wflaj}x`9rbgj|7  
```
# Solution
We know that we have to ROT every digit, the only thing is that the number in the rotation is different for every character.

A piece of cake is the big hint to reach the solution. While a pie it's not a dessert, it's close enough to think that it's referring to the number pi **π**.

Rather that ROT'ing by hand every character with cyberchef, let's have a python script do it instead.

```
encoded_flag = "ii35;6Ykf|h~j8adgf7ve5uuiw37wflaj}x`9rbgj|7  "
# first 47 digits of pie
PIE = "14159265358979323846264338327950288419716939937"

def rot(letter, number):
    #turn letter to ascii decimal value
    letter = ord(letter)
    #substracting the ascii decimal value a number of times will rotate it by that much
    rotated = letter - int(number)
    return chr(rotated)

flag = ''    
for i in enumerate(encoded_flag):
    flag += rot(i[1], PIE[i[0]])

print(flag)
```

Which returns the flag `he2024{That_wa5_a_b1t_1rrat10nal_but_0kaaay.}↔↓`