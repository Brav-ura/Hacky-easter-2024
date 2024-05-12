def unscramble():    
    flag = "da.,.0w`-vv[evv[luj^&dUZ'pp*pp)cXb'ds"
    l = list(flag)

    leet = 1 # Last value of leet after the final leet = leet//10

    #Transformations will be done in reverse order from the original script
    for i in range(len(l)):
        # The inverse operation of XOR is another XOR
        l[i] = chr(ord(l[i]) ^ (i % (leet % 10)))

    leet  = 13 # penultimate value of leet = leet//10
    #No need to reverse the operation of the range, as we want to make sure to also transform from the middle of the string to the end
    for i in range(len(l)//2,len(l)):
        #rather than substract, add
        l[i] = chr((ord(l[i]) + (leet % 10)))
    leet = 133 # second value of leet = leet//10

    for i in range(len(l)//2):
        # this time substract, not add
        l[i] = chr((ord(l[i]) - (leet % 10)))
    leet = 1337 # original constant

    for i in range(len(l)):
        # add again
        l[i] = chr((ord(l[i]) + (leet % 10)))

    print(''.join(l))
unscramble()
