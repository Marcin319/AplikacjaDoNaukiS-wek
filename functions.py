import random
import os
import linecache
def odgadnijAP(LS,wybor4):
    m = zapytanie()
    n=0
    while n!=m:
        n=losENGPL(n,LS,m,wybor4)
        ciągD(n,m)
def odgadnijPA(LS,wybor4):
    m=zapytanie()
    n = 0
    while n != m:
        n=losPLENG(n,LS,m,wybor4)
        ciągD(n,m)
def odgadnijRAN(LS,wybor4):
    m=zapytanie()
    n = 0
    while n != m:
        ran=random.randrange(2)
        if ran==0:
            n=losENGPL(n,LS,m,wybor4)
        else:
            n=losPLENG(n,LS,m,wybor4)
        ciągD(n,m)
def losPLENG(n,LS,m,wybor4):
    x = random.randint(2, LS)
    while x % 2 == 1:
        x = random.randint(2, LS)
    print(linecache.getline(wybor4,x))
    input("Odpowiedź: ")
    print("Poprawna odpowiedź: ",linecache.getline(wybor4,x-1))
    if n<m:
        n += 1
    return n
def losENGPL(n,LS,m,wybor4):
    x = random.randint(2, LS)
    while x % 2 == 0:
        x = random.randint(2, LS)
    print(linecache.getline(wybor4, x))
    input("Odpowiedź: ")
    print("Poprawna odpowiedź: ", linecache.getline(wybor4, x+1))
    if n<m:
        n += 1
    return n
def ciągD(n,m):
    if n < m:
        input("Dalej: ENTER")
        os.system('cls')
    else:
        input("\n\nAby powrócić do menu, naciśnij ENTER")
        os.system('cls')
def zapytanie():
    os.system('cls')
    try:
        m = int(input("Ile razy mam Cię zapytać?: "))
        os.system('cls')
    except:
        m=zapytanie()
    return m
def liczlinijki(wybor4):
    qe=0
    plik=open(wybor4,"r")
    for i in plik:
        qe+=1
    plik.close()
    return qe
def wyjscieZsesji(czywyj,n,m):
    if czywyj=="ex":
        n=m
    return n