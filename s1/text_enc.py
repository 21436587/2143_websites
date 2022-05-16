while True:
    c = input(    "Text? :")
    em=3
    d = c
    e = ""
    co=0
    for i in d:
        if co%4==0:
            e += chr(ord(i) ^ 1*em)
        if co%4==1:
            e += chr(ord(i) ^ 8*em)
        if co%4==2:
            e += chr(ord(i) ^ 2*em)
        if co%4==3:
            e += chr(ord(i) ^ 4*em)
        co+=1
    co=0
    print("Out:"+str(" "*(len("Text? :")-len("Out:")))+e.replace("⌂","g"))
    #ÛÚ¤
    c=""
    d=""
    print("="*len("Out:"+str(" "*(len("Text? :")-len("Out:")))+e))