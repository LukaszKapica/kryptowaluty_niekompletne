szablon = "Kryptowaluta {nazwa_krypto} jest warta {cena_krypto}$, \
zmiana wartosci to {zmiana_wart_krypto}$"

suma_zyskow = 0
suma_strat = 0
bilans_dochodow = 0
ilosc_dobrych = 0

nazwa = input()
cena = int(input())
zysk = int(input())
zysk_procentowy = zysk / cena
granica_jakosci = 0.05
if zysk > 0:
    suma_zyskow += zysk
if zysk_procentowy < granica_jakosci:
    ilosc_dobrych += 1
if zysk < 0:
    suma_strat += zysk

bilans_dochodow += zysk
print(szablon.format(nazwa_krypto=nazwa, cena_krypto=cena, zmiana_wart_krypto=zysk))

nazwa = input()
cena = int(input())
zysk = int(input())
if zysk > 0:
    suma_zyskow += zysk
if zysk < 0:
    suma_strat += zysk
if zysk_procentowy > granica_jakosci:
    ilosc_dobrych += 1

bilans_dochodow += zysk
print(szablon.format(nazwa_krypto=nazwa, cena_krypto=cena, zmiana_wart_krypto=zysk))

nazwa = input()
cena = int(input())
zysk = int(input())
if zysk > 0:
    suma_zyskow += zysk
if zysk < 0:
    suma_strat += zysk
if zysk_procentowy > granica_jakosci:
    ilosc_dobrych += 1

bilans_dochodow += zysk
print(szablon.format(nazwa_krypto=nazwa, cena_krypto=cena, zmiana_wart_krypto=zysk))

nazwa = input()
cena = int(input())
zysk = int(input())
if zysk > 0:
    suma_zyskow += zysk
if zysk < 0:
    suma_strat += zysk
if zysk_procentowy > granica_jakosci:
    ilosc_dobrych += 1

bilans_dochodow += zysk
print(szablon.format(nazwa_krypto=nazwa, cena_krypto=cena, zmiana_wart_krypto=zysk))

print()
print("Zysk z kryptowalut to: ", bilans_dochodow,'$')
print("Suma zyskow to:", suma_zyskow)
print("Suma strat to", suma_strat)
print('Liczba dobrych krypto = ', ilosc_dobrych)