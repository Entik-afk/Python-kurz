vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')

cislo_dne = int(input("zadejte cislo dne: "))

if cislo_dne <= 7:
    cislo = cislo_dne-1
else:
    cislo = (cislo_dne % 7 )+1


if cislo_dne in vstupni_cisla:
    den = True
    print("Správná vstupní hodnota!")
else:
    den = False
    print("Spatna vstupní hodnota!")

if cislo_dne <= 7:
    den_tydne = tyden[cislo]
else:
    den_tydne = tyden[cislo]

pismeno_cislo = den_tydne[0]

if pismeno_cislo == vstupni_pismena[cislo]:
    print("Správné písmeno")

else:
    print("Špatné písmeno")

print(den)
print(den_tydne)
print(pismeno_cislo)
