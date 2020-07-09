lokalizacja = input("Lokalizacja pliku z danymi wejściowymi: ")
lokalizacja2 = input("Lokalizacja pliku z poprawnymi odpowiedziami: ")

plik = open(lokalizacja)
inpx = plik.readlines()
inp = inpx[0].strip()
znaki1 = ["a", "e", "i", "o", "s"]
znaki2 = ["4", "3", "1", "0", "5"]
licznik = 0
for u in range(len(inp)):
        while licznik != len(znaki1):        
                if inp[u] == znaki1[licznik]:
                        inp = inp[:u] + znaki2[licznik] + inp[u + 1:]
                licznik += 1
        licznik = 0

plik2 = open(lokalizacja2)
odpx = plik2.readlines()
odp = odpx[0].strip()

if inp == odp:
        print("Dobrze!!!!!!")