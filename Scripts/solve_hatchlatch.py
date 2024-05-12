from random import *

def make_cipher(flag):
    cipher=[]
    #kee=randint(1,10000)
    kee=1337
    #off=randint(1,5)
    off=3
    for f in flag:
        cipher.append(str((ord(f) - off) ^ kee))
    return(cipher)

cipher_flag = ['6255', '6248', '6181', '6183', '6181', '6203', '6258', '6255', '6203', '6267', '6250', '6255', '6230', '6203', '6250', '6250', '6202', '6200', '6200', '6230', '6254', '6245', '6203', '6241', '6267', '6202', '6251', '6256']

def decipher(ciphered, kee, off):
    deciphered=[]
    for i in ciphered:
        decrypted = int(i) ^ kee # make it to a number rather than a string. Then, the inverse of a XOR is another XOR
        decrypted += off # sum the offset
        decrypted_char = chr(decrypted) #convert back to a character
        deciphered.append(decrypted_char)
    return deciphered

print(''.join(decipher(make_cipher("he2024{test_flag}"),1337,3)))

for kee in range(1,10000):
    for off in range(1,5):
        flag = ''.join(decipher(cipher_flag, kee, off))
        if 'he2024' in flag:
            print(flag)