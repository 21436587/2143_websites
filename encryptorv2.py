while True:
    import os as r
    r.system("mode con: cols=64 lines=16")
    c = input(">>>")
    n = int(input("incrament (shifting)"))
    d = []
    for l in c: 
        d.append(ord(l)^n+n//2)
    print()
    e = ""
    for k in d:
        e+=chr(k)
    print(e)
    input()
