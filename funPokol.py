import functions as fc
import linecache
def pokoleiPLENG(LS,wybor4):
    i=2
    while i<=LS:
        print(linecache.getline(wybor4, i))
        czywyj = str(input("Odpowiedź: "))
        i = fc.wyjscieZsesji(czywyj, i, LS)
        print("Poprawna odpowiedź: ", linecache.getline(wybor4, i-1))
        if i < LS:
            i += 2
        else:
            i+=1
        fc.ciągD(i,LS)
def pokoleiENGPL(LS,wybor4):
    i=1
    while i<=LS:
        print(linecache.getline(wybor4, i))
        czywyj=str(input("Odpowiedź: "))
        i=fc.wyjscieZsesji(czywyj,i,LS)
        print("Poprawna odpowiedź: ", linecache.getline(wybor4, i+1))
        if i<LS:
            i+=2
        else:
            i+=1
        fc.ciągD(i,LS)