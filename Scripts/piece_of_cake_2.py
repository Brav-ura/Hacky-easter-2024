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