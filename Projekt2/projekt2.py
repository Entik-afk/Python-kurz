"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lech Gajdzica
email: lech.gajdzica@hotmail.com
"""

import random

oddelovac = 30 * "-"

"""" program pozdraví užitele a vypíše úvodní text  (viz. níže v ukázkách)"""

print("Ahoj Hráči")
print(oddelovac)
print("Vytvořil jsem pro tebe hru!")
print("Zahrajeme si bull and cows, takže budeš muset uhádnout čtyřmístnou číslici.")
print("Bulls indikuje, kolik číslic jsi uhádl a jsou na správném místě. Pokud jsi uhádl číslici, ale není na místě, kde by měla být, uhádl jsi cows.")
print("Hádané číslo nesmí začínat 0, číslice se nesmí opakovat.")
print(oddelovac)

def hadane_cislo(od, do, x):
    
    seznam = list(range(od, do))

    random.shuffle(seznam)

    return seznam[:x]


tajne = hadane_cislo(0,10,4)
if tajne[0] == 0:
    tajne = hadane_cislo(0,10,4)



str_tajne = [str(x) for x in tajne]
tajne_cislo = int( "".join(str_tajne))



"""hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla,
pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky,
"""


def tipuj():
    tip = str(input("Zadej hádané číslo: "))
    kontrola = True
    if len(tip) == 4 and int(tip[0]) != 0 and tip.isnumeric() and tip[0] != tip[1] and tip[0] != tip[2] and tip[0] != tip[3] and tip[1] != tip[2] and tip[1] != tip[3] and tip[2] != tip[3]:
        
        kontrola = True
    else:
        exit("Nesprávný formát čísla, zahraj si znovu")
        kontrola = False
    return tip


"""bulls - číslo + umístění"""
bulls = 0


def kolik_bulls():
    bulls=0
    y = 0
    cislo_list_tip = [ int(x) for x in list_tip]
    while y < 4:
        if cislo_list_tip[y] == tajne[y]:
            
            bulls = bulls + 1
            y = y + 1
        else:
            y = y +1
        
    return bulls


def vyhodnoceni_bulls():
    if bulls > 1 and bulls < 4:
        print(f"Uhádl jsi {bulls} bulls")
    elif bulls == 4:
        print(f"Tajné číslo bylo {tajne_cislo}")
        exit("Vyhrál jsi")
        
    else:
        print(f"Uhádl jsi {bulls} bull")



def kolik_cows():
    cows = 0
    z = 0
    cislo_list_tip = [ int(x) for x in list_tip]
    while z < 4:

        if cislo_list_tip[z] in tajne:
            cows  = cows + 1
            z = z +1
        else:
            z = z + 1

    return cows



def vyhodnoceni_cows():
    if cows <= 1:
        print(f"Uhádl jsi {cows} cow")
    else:
        print(f"Uhádl jsi {cows} cows")


pocet_tipu = 0
while bulls < 4:
    bulls = 0
    cows = 0
    
    
    tip = tipuj()
    
    list_tip = list(tip)
    
    bulls = kolik_bulls()
    cows = kolik_cows() - bulls
    
    vyhodnoceni_bulls()
    vyhodnoceni_cows()
    
    pocet_tipu = pocet_tipu + 1
    print(f"Počet tipů je {pocet_tipu}")
    print(oddelovac)

