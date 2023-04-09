import os as r
import time as t
import ctypes
import sys 
from ctypes import c_long, c_wchar_p, c_ulong, c_void_p


#==== GLOBAL VARIABLES ======================

gHandle = ctypes.windll.kernel32.GetStdHandle(c_long(-11))

# ???????nnnn???????? ??????????? ????
console = ctypes.windll.kernel32.GetStdHandle(-11)

# ??????? ????????? CONSOLE_CURSOR_INFO
class CONSOLE_CURSOR_INFO(ctypes.Structure):
    _fields_ = [("dwSize", ctypes.c_ulong),
                ("bVisible", ctypes.c_bool)]

def blink(m=True):
    # ??????? ????????? ????????? CONSOLE_CURSOR_INFO
    cci = CONSOLE_CURSOR_INFO()
    cci.dwSize = 100
    cci.bVisible = m

    # ????????????? ????? ????????? ??????
    ctypes.windll.kernel32.SetConsoleCursorInfo(console, ctypes.byref(cci))


def move (x,y): ########################################################### do not touch this it's a reserved code
   """Move cursor to position indicated by x and y."""
   value = x + (y << 16)
   ctypes.windll.kernel32.SetConsoleCursorPosition(gHandle, c_ulong(value))
r.system("mode con: cols=20 lines=4")
r.system("cls")
r.system("color 17")
move(0,0)
blink(False)

MANIFACTUER = "Sparch!"
VERSION     = "1.0"

print(f"PPC v{VERSION}")
print("Type help to help")

###Setup

ins = [None]*100
def error(desc):
    print(f"@  {desc}")
t.sleep(0.8)
blink(True)

### Registers

CRI = 0  #CR Integer
CRS = "" #CR String
LC  = -1
LDF = False
inm = "none"

import keyboard as kb

def page(s):
    n = 20
    for m in [s[i:i+n] for i in range(0, len(s), n)]:
        print(m,end="",flush=True)
eut = ""
while True:
    try:
        if LDF:
            parserraw = eut[LC]
        else:
            parserraw = input(";  ")
    except KeyboardInterrupt:
        error("interrupt")
    blink(False)
    try:
        parser=parserraw.split()
        parser[0]
    except:
        error("empty line")
        blink(True)
        continue
    if "$i;" in parserraw:
        inm = int(input(";> "))
    elif "$s;" in parserraw:
        inm = input(";> ")
     
    ############################################################ if you travel beyond this point you will die
    
    if parser[0]=="store":
        try:
            insn = int(parser[1])
            if parser[2]=="str":
                ins[insn] = parserraw.replace(parser[0]+" "+parser[1]+" "+parser[2]+" ","").replace("$s;",inm)
            if parser[2]=="int":
                try:
                    ins[insn] = int(parserraw.replace(parser[0]+" "+parser[1]+" "+parser[2]+" ","").replace("$i;",inm))
                except:
                    error("wrong type")
        except:
            try:
                int(parser[1])
            except:
                error("fail at arg n1")
            try:
                parser[2]
            except:
                error("fail at arg n2")
    elif parser[0]=="read":
        insn = int(parser[1])
        if ins[insn]==None:
            error("empty")
        else:
            if type(ins[insn]) is int:
                CRI = ins[insn]
            if type(ins[insn]) is str:
                CRS = ins[insn]
    elif parser[0]=="print":
        print("> "+parserraw.replace(parser[0],"").replace(r"%i;",str(CRI)).replace(r"%s;",str(CRS)))
    elif parser[0]=="reload" or parser[0]=="restart":
        r.startfile(__file__)
        sys.exit()
    elif parser[0]=="help":
        r.system("help.txt")
    elif parser[0]=="parser": # do not touch that shit again
        d = 10-len(f"v{VERSION}")
        d2 = 14-len(f"Made by\n {MANIFACTUER}")
        print(" "*d+f"v{VERSION}")
        print(" "*d+f"Made by\n"+" "*d+f"{MANIFACTUER}")
        d = None
        d2 = None
    elif parser[0]=="calculate":
        try:
            IS = parserraw.replace(parser[0],"").replace(r"%i;",str(CRI)).replace(r"$s;",inm)
            CRI= int(eval(IS))
        except BaseException as e:
            error("not valuable")
            r.system("pause>Nul")
            error(f"see {e}")
            r.system("pause>Nul")
    elif parser[0]=="jmp":
        if not LDF:
            error("available in")
            error("rom mode")
        else:
            try:
                if not kb.is_pressed("q"):
                    LC = int(parser[1])
                else:
                    error("aborted jmp")
            except:
                error("nonexistent")
    elif parser[0]=="if":
        if not LDF:
            error("available in")
            error("rom mode")
        else:
            try:
                IS = parserraw.replace(parser[0]+" "+parser[1]+" "+parser[2],"").replace(r"%i;",str(CRI)).replace(r"$s;",inm)
                CRI= int(eval(IS))
                if CRI>0:
                    LC = int(parser[1])
                else:
                    LC = int(parser[2])
            except:
                error("nonexistent")
                error("or not val.")
    elif parser[0]=="end":
        if not LDF:
            error("available in")
            error("rom mode")
        else:
            r.system("pause>Nul")
            LDF=False    
    elif parser[0]=="cls":
        print("\n\n\n\n\n")
    elif parser[0]=="load":
        LDF = True
        LC = -1
        f = open("pcc.rom","r")
        eut = f.read().splitlines()
        f.close()
    elif parser[0]=="dir":
        dir_path = r.path.dirname(r.path.realpath(__file__))
        import os.path
        alle = [d for d in r.listdir(dir_path) if r.path.isdir(r.path.join(dir_path, d))]
        c = 0
        for d in alle:
            print(f"|  {d[0:16]}")
            if c==2:
                r.system("pause>Nul")
            c+=1
            c%=3
    elif parser[0]=="cd":
        r.system(f"cd {parserraw.replace(parser[0],'')}")
    else:
        error("unknown command")
    blink(True)  
    LC += 1
