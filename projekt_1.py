"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lech Gajdzica
email: lech.gajdzica@hotmail.com
"""

oddelovac = "-" * 50

uzivatele = { "bob" : "123" , "ann": "pass123" , "mike" : "password123" , "liz" : "pass123"}

jmeno = input("Zadejte jmeno: ").lower()
heslo = input("Zadejte heslo: ")

print(oddelovac)

if jmeno in uzivatele and heslo == uzivatele[jmeno]:
    print("Overeni probehlo v poradku muzes analizovat texty ")
else:
    print("Nejste registrovan")
    quit()

print(oddelovac)

print(f"Vitej {jmeno}")





TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


delka = len(TEXTS) #kolik je celkem textu

#print(delka)
print(oddelovac)
print(f"Vyber jeden z {delka} textu")
vyber_textu = int(input(f"Zadejte cislo 1 az {delka}: "))

print(oddelovac)

if vyber_textu <= delka:
    print(f"Vybral jsi text {vyber_textu}")
else:
    print("Vybrali jste cislo mimo vyber")
    quit()

#print(vyber_textu)

vybrany_text = TEXTS[vyber_textu-1]

#print(vybrany_text)
#print(type(vybrany_text))

vybrany_split = vybrany_text.replace("-"," ").split() # rozdeleni textu na jendotlive slova

analizovat_text = [slovo.strip(",.-") for slovo in vybrany_split]

#print(type(analizovat_text))

pocet_slov = len(analizovat_text) #celkem pocet slov

print(f"Celkove je v textu {pocet_slov} slov")

titul_pismeno = int(0) #Velkz na zacatku

for slovo in analizovat_text:
    if slovo.istitle():
        #print("ano")
        titul_pismeno = titul_pismeno + 1
    else:
        continue

velkym_slovo = int(0) #vsechny velke

for slovo in analizovat_text:
    if slovo.isupper() and slovo.isalpha():
        velkym_slovo = velkym_slovo + 1
    else:
        continue
malym_slovo = int(0) # vsechny male

for slovo in analizovat_text:
    if slovo.islower() and slovo.isalpha:
        malym_slovo = malym_slovo + 1
    else:
        continue

pocet_cisel = int(0) #pocet 3cisel
suma_cisel = [] # suma cisel

for slovo in analizovat_text:
    if slovo.isnumeric():
        pocet_cisel = pocet_cisel + 1
        suma_cisel.append(int(slovo))
    else:
        continue


print(f"Celkem slov zacinajici Velkym pismenem: {titul_pismeno}")
print(f"Pocet slov psano vsechno velkym: {velkym_slovo}")
print(f"Pocet slov psanych malym pismem: {malym_slovo}")
print(f"V textu jsem {pocet_cisel} ciselne stringy")
print(f"Suma vsech cisel je: {sum(suma_cisel)}")

print(oddelovac)

maximalni_delka_slova = max(analizovat_text, key=len)
#print(maximalni_delka_slova)
#print(type(maximalni_delka_slova))

maximalni_delka_slova_pocet = len(maximalni_delka_slova)



for slovo in analizovat_text:
    if slovo.isalpha():
        delka = max(analizovat_text, key=len)

#print(delka)      
#print(maximalni_delka_slova_pocet)
#print(type(maximalni_delka_slova_pocet))

pocet_slov_list = []

pocet_slov_list = [0] * (maximalni_delka_slova_pocet)

for slovo in analizovat_text: #delka slova
    if slovo.isalnum():
        x = len(slovo)
        pocet_slov_list[x-1] = pocet_slov_list[x-1] + 1
    else:
        continue


#print(analizovat_text)
#print(pocet_slov_list)
#print(type(pocet_slov_list))

#print(oddelovac)

max_pocet_slov = max(pocet_slov_list)
#print(max_pocet_slov)

z = 1
print(f"LEN|".rjust(4), "OCCURENCES".center(max_pocet_slov + 1), "|NR".ljust(5))
print(oddelovac)
for x in pocet_slov_list:
    
    print(f"{z}|".rjust(4), ("*" * x).ljust(max_pocet_slov + 1), f"|{x}".ljust(5))
    z = z + 1