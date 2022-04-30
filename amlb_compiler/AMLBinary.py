import random as r
import sys as s
import os
os.system("mode con: cols=64 lines=16")
arg = s.argv[1]
string = open(arg, encoding="ansi", mode="r").read()
c      = 0
c2     = 0
rec    = 0
srec   = 0
recstr = ""
c3     = [0, 0, 0, 0, 0, 0, 0, 0] #hardcore memory in uhhhhhhhhhhhhhhh... 2^31^8?
def test():
    global c3
    print(f"1 {c3.count(0)} places of memory is using")
    print( "2 memory test")
    def memtest():
        try:
            for i in range(0,50000):
                c3[r.randint(0,c3.count(0))]=r.randint(-10000,10000)
                c3[r.randint(0,c3.count(0))]=0
        except:
            print("|\n\\- trying to redo...")
            memtest()
    memtest()
    print("3 ready to go")
    if string=="":
        print("no programm was writed")
        input()
        exit()
    c3     = [0, 0, 0, 0, 0, 0, 0, 0]
    raw = string.replace('\n','.')
    print(f"the string is {raw}")
test()
print("starting programm\n|\n|\n|\n")
c3     = [0, 0, 0, 0, 0, 0, 0, 0]
errors = ["", ""]
def lex(string):
    """
    X00 CURSOR+1
    X01 CURSOR-1
    X02 MEM VALUE+1
    X03 MEM VALUE-1
    X04 MULTIPLY BY 2
    X05 DIVIDE BY 2
    X06 PRINT NEXT PLACE (NEXT CHARACTER)
    X07 PRINT MEMORY (CHARACTER)
    X08 SET MEMORY NEXT PLACE (NEXT CHARACTER)
    X09 SET MEMORY IN-PLACE
    X0A SET MEMORY TO 0
    X0B SET MEMORY FROM STR INPUT
    X0C SET MEMORY FROM INT INPUT
    X0D EMPTY
    X0E }
    X0F {
    X10  EMPTY
    X11  EMPTY
    X12  EMPTY
    X13  EMPTY
    X14  EMPTY
    X15  EMPTY
    X16  EMPTY
    X17  EMPTY
    X18  EMPTY
    X19  EMPTY
    X1A  EMPTY
    X1B  EMPTY
    X1C  EMPTY
    X1D  EMPTY
    X1E  EMPTY
    X1F  EMPTY


    V
    """

    global c2
    global c
    global rec
    global recstr
    global srec
    global errors
    for i in string:
        if i=="\xff": # MEMORY FILLER (EMPTY)
            pass
        if i=="\x00": # CURSOR+1
            try:
                c+=1
            except:
                errors.append(f"[ERROR {c2}] Can't go outside of list")
        if i=="\x01": # CURSOR-1
            try:
                c-=1
            except:
                errors.append(f"[ERROR {c2}] Can't go outside of list")
        if i=="\x02": # MEM VALUE+1
            try:
                c3[c]+=1
            except:
                errors.append(f"[ERROR {c2}] Number is bigger than long long (С++)")
        if i=="\x03": # MEM VALUE-1
            try:
                c3[c]+=1
            except:
                errors.append(f"[ERROR {c2}] Number is smaller than long long (С++)")
        if i=="\x04": # MULTIPLY BY 2
            try:
                c3[c]*=2
            except:
                errors.append(f"[ERROR {c2}] Number is bigger than long long (С++)")
        if i=="\x05": # DIVIDE BY 2
            try:
                c3[c]//=2
            except:
                errors.append(f"[ERROR {c2}] Number is smaller than long long (С++)")
        if i=="\x06": # PRINT NEXT PLACE (NEXT CHARACTER)
            try:
                print(string[c2+1],end="")
            except:
                errors.append(f"[ERROR {c2}] Non-existent slot of memory")
        if i=="\x07": # PRINT MEMORY (CHARACTER)
            try:
                print(chr(c3[c]),end="")
            except:
                errors.append(f"[ERROR {c2}] Invalid slot of memory")
        if i=="\x08": # SET MEMORY NEXT PLACE (NEXT CHARACTER)
            try:
                c3[c]=ord(string[c2+1])
            except:
                errors.append(f"[ERROR {c2}] Non-existent slot of memory")
        if i=="\x09": # SET MEMORY TO RANDOM (-255 - +255)
            try:
                c3[c]=r.randint(-255,255)
            except:
                errors.append(f"[ERROR {c2}] Invalid slot of memory")
        if i=="\x0a": # SET MEMORY TO 0
            try:
                c3[c]=0
            except:
                errors.append(f"[ERROR {c2}] Invalid slot of memory / non-existent slot of memory")
        if i=="\x0b": # SET MEMORY FROM STR INPUT
            try:
                c3[c]=input()
            except:
                errors.append(f"[ERROR {c2}] Console have no output / invalid slot of memory")
        if i=="\x0c": # SET MEMORY FROM INT INPUT
            try:
                c3[c]=int(input())
            except:
                errors.append(f"[ERROR {c2}] Console have no output / invalid slot of memory")
        if i=="\x0d": # -EMPTY-
            pass
        if i=="\x0e": # }
            try:
                rec=0
                try:
                    lex(recstr)
                except:
                    errors.append(f"[ERROR] Loop uncompilable")
                    break
            except:
                errors.append(f"[ERROR {c2}] Record is invalid")
        if i=="\x0f": # IF MEM VALUE>0 THEN{
            try:
                if int(c3[c])>0: rec=1
            except:
                errors.append(f"[ERROR {c2}] Record is invalid")
        if rec==1 and srec==1:
            try:
                recstr+=i
            except:
                errors.append(f"[ERROR {c2}] Surrogates not allowed / Character ord. is bigger that 0x110000")
        srec=1
        c2+=1
    с2 = 0
    if rec==1:
        errors.append(f"[ERROR {c2}] Closing loop character not detected")
    return errors
for i in lex(string):
    print(i)
input("\n")