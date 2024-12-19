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


print(oddelovac)
print(f"Vyber jeden z {delka} textu")
vyber_textu = int(input(f"Zadejte cislo 1 az {delka}: "))

print(oddelovac)

if vyber_textu <= delka and vyber_textu > 0:
    print(f"Vybral jsi text {vyber_textu}")
else:
    print("Vybrali jste cislo mimo vyber")
    quit()



vybrany_text = TEXTS[vyber_textu-1]



vybrany_split = vybrany_text.replace("-"," ").split() # rozdeleni textu na jendotlive slova

analizovat_text = [slovo.strip(",.-") for slovo in vybrany_split]



pocet_slov = len(analizovat_text) #celkem pocet slov

print(f"Celkove je v textu {pocet_slov} slov")

titul_pismeno = int(0) #Velkz na zacatku
malym_slovo = int(0) # vsechny male
velkym_slovo = int(0) #vsechny velke

pocet_cisel = int(0) #pocet 3cisel
suma_cisel = [] # suma cisel

for slovo in analizovat_text:
    if slovo.istitle():
        titul_pismeno = titul_pismeno + 1
    elif slovo.isnumeric():
        pocet_cisel = pocet_cisel + 1
        suma_cisel.append(int(slovo))
    elif slovo.islower() and slovo.isalpha:
        malym_slovo = malym_slovo + 1
    elif slovo.isupper() and slovo.isalpha():
        velkym_slovo = velkym_slovo + 1
    else:
        continue


print(f"Celkem slov zacinajici Velkym pismenem: {titul_pismeno}")
print(f"Pocet slov psano vsechno velkym: {velkym_slovo}")
print(f"Pocet slov psanych malym pismem: {malym_slovo}")
print(f"V textu jsem {pocet_cisel} ciselne stringy")
print(f"Suma vsech cisel je: {sum(suma_cisel)}")

print(oddelovac)

maximalni_delka_slova = max(analizovat_text, key=len)


maximalni_delka_slova_pocet = len(maximalni_delka_slova)



for slovo in analizovat_text:
    if slovo.isalpha():
        delka = max(analizovat_text, key=len)



pocet_slov_list = []

pocet_slov_list = [0] * (maximalni_delka_slova_pocet)

for slovo in analizovat_text: #delka slova
    if slovo.isalnum():
        x = len(slovo)
        pocet_slov_list[x-1] = pocet_slov_list[x-1] + 1
    else:
        continue




max_pocet_slov = max(pocet_slov_list)


z = 1
print(f"LEN|".rjust(4), "OCCURENCES".center(max_pocet_slov + 1), "|NR".ljust(5))
print(oddelovac)
for x in pocet_slov_list:
    
    print(f"{z}|".rjust(4), ("*" * x).ljust(max_pocet_slov + 1), f"|{x}".ljust(5))
    z = z + 1