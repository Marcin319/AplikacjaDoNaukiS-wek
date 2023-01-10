import os
def tworzenieKat():
    os.system('cls')
    nowy = str(input("Podaj nazwę nowego slownika:\n"))
    czek = open("listakategorii.txt","r")
    n=0
    for i in czek:
        if i==nowy:
            n+=1
    if n!=0:
        print("Taka kategoria już istnieje")
        czek.close()
    else:
        czek.close()
        nowy2 = nowy + ".txt"
        plik = open(nowy2, "w")
        czek=open("listakategorii.txt","a")
        czek.write("\n")
        czek.write(nowy)
        czek.close()
        plik.close()
def dodawanieSlowek():
    os.system('cls')
    czydobrz=0
    x=0
    while czydobrz==0:
        listasl = open("listakategorii.txt", "r")
        for i in listasl:
            print(i)
            print("\n")
        wybor=(input("Wybierz kategorię:\n"))
        wybor2 = wybor + ".txt"
        print(wybor2)
        try:
            z=open(wybor2,"r")
            print(z)
        except:
            os.system('cls')
            print("Taka kategoria nie istnieje")
        z.close()
        plik=open(wybor2,'a')
        while czydobrz==0:
            os.system('cls')
            print(wybor)
            r=int(input("\t1. Dodaj słówko\n\t2. Wyjście do menu\n"))
            os.system('cls')
            if r==1:
                slowoOB=str(input("Podaj słowo obce:\n"))
                slowoOJ=str(input("Podaj tłumaczenie na język ojczysty:\n"))
                plik.write(slowoOB+"\n")
                plik.write(slowoOJ+"\n")
            else:
                czydobrz+=1
    listasl.close()
    plik.close()