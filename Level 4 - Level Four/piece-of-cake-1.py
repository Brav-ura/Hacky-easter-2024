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