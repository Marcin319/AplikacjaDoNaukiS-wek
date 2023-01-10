import functions as fc
import funPokol as fP
import os
import obslugaslowek as obsl
x=0
while x==0:
    print("\tMENU:\n1. Graj\n2. Zarządzanie kategoriami i słówkami\n0. WYJDŹ")
    wybor=int(input())
    if wybor==1:
        print("Wybierz kategorię:")
        kat=open("listakategorii.txt","r")
        for i in kat:
            print("\t"+i)
        wybor3=str(input())
        wybor4=wybor3+".txt"
        LS = fc.liczlinijki(wybor4)
        try:
            z=open(wybor4,"r")
            print(z)
        except:
            os.system('cls')
            print("Taka kategoria nie istnieje")
        z.close()
        os.system('cls')
        print("1. Zgadnij z obcego na ojczysty\n2. Zgadnij z ojczystego na obcy\n3. Zgaduj losowo")
        wybor5=int(input())
        if wybor5==1:
            os.system('cls')
            print(
                "1. Zgadnij z obcego na ojczysty\n\t1. Zgadywanie określonej liczby słówek losowo\n\t2. Odpowiadanie na wszystkie slowka po kolei")
            wybor2 = int(input())
            if wybor2 == 1:
                fc.odgadnijAP(LS,wybor4)
            elif wybor2 == 2:
                fP.pokoleiENGPL(LS,wybor4)
        elif wybor5 == 2:
            os.system('cls')
            print(
                "2. Zgadnij z ojczystego na obcy\n\t1. Zgadywanie określonej liczby słówek losowo\n\t2. Odpowiadanie na wszystkie slowka po kolei")
            wybor2 = int(input())
            if wybor2 == 1:
                fc.odgadnijPA(LS,wybor4)
            elif wybor2 == 2:
                fP.pokoleiPLENG(LS,wybor4)
        elif wybor5 == 3:
            fc.odgadnijRAN(LS,wybor4)
        else:
            os.system('cls')
    if wybor==2:
        os.system('cls')
        print("2.Zarządzanie kategoriami\n\t1. Tworzenie kategorii\n\t2. Dodawanie słówek\n\t0. Powrót do menu")
        wybor2=int(input())
        if wybor2==1:
            obsl.tworzenieKat()
        elif wybor2==2:
            obsl.dodawanieSlowek()
        else:
            os.system('cls')
    elif wybor!=1 and wybor!=2:
        exit()