"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lech Gajdzica
email: lech.gajdzica@hotmail.com
"""

import random
from typing import List

oddelovac = 30 * "-"

def uvodni_text() -> None:
    """
    Vypíše úvodní text hry.
    """
    print("Ahoj Hráči")
    print(oddelovac)
    print("Vytvořil jsem pro tebe hru!")
    print("Zahrajeme si bull and cows, takže budeš muset uhádnout čtyřmístnou číslici.")
    print("Bulls indikuje, kolik číslic jsi uhádl a jsou na správném místě. Pokud jsi uhádl číslici, ale není na místě, kde by měla být, uhádl jsi cows.")
    print("Hádané číslo nesmí začínat 0, číslice se nesmí opakovat.")
    print(oddelovac)

def hadane_cislo(od: int, do: int, x: int) -> List[int]:
    """
    Vygeneruje seznam náhodných unikátních číslic.

    Args:
        od (int): Začátek rozsahu (včetně).
        do (int): Konec rozsahu (včetně).
        x (int): Počet číslic k vygenerování.

    Returns:
        List[int]: Seznam vygenerovaných číslic.
    """
    seznam = list(range(od, do))
    random.shuffle(seznam)
    return seznam[:x]

def tipuj() -> str:
    """
    Požádá hráče o hádané číslo a zkontroluje jeho formát.

    Returns:
        str: Hráčův tip.
    """
    while True:
        tip = input("Zadej hádané číslo: ")
        if len(tip) == 4 and tip.isnumeric() and int(tip[0]) != 0 and len(set(tip)) == 4:
            return tip
        else:
            print("Nesprávný formát čísla, zkus to znovu.")

def kolik_bulls(list_tip: List[int], tajne: List[int]) -> int:
    """
    Spočítá počet "bulls" (správných číslic na správném místě).

    Args:
        list_tip (List[int]): Hráčův tip jako seznam číslic.
        tajne (List[int]): Tajné číslo jako seznam číslic.

    Returns:
        int: Počet bulls.
    """
    bulls = sum(1 for i in range(4) if list_tip[i] == tajne[i])
    return bulls

def vyhodnoceni_bulls(bulls: int, tajne_cislo: int) -> None:
    """
    Vypíše hráči počet "bulls" a kontroluje, zda hráč vyhrál.

    Args:
        bulls (int): Počet bulls.
        tajne_cislo (int): Tajné číslo.
    """
    if bulls == 4:
        print(f"Tajné číslo bylo {tajne_cislo}")
        exit("Vyhrál jsi")
    elif bulls > 1:
        print(f"Uhádl jsi {bulls} bulls")
    else:
        print(f"Uhádl jsi {bulls} bull")

def kolik_cows(list_tip: List[int], tajne: List[int]) -> int:
    """
    Spočítá počet "cows" (správných číslic na špatném místě).

    Args:
        list_tip (List[int]): Hráčův tip jako seznam číslic.
        tajne (List[int]): Tajné číslo jako seznam číslic.

    Returns:
        int: Počet cows.
    """
    cows = sum(1 for cislo in list_tip if cislo in tajne) - kolik_bulls(list_tip, tajne)
    return cows

def vyhodnoceni_cows(cows: int) -> None:
    """
    Vypíše hráči počet "cows".

    Args:
        cows (int): Počet cows.
    """
    if cows == 1:
        print(f"Uhádl jsi {cows} cow")
    else:
        print(f"Uhádl jsi {cows} cows")

def hra() -> None:
    """
    Spustí hlavní logiku hry.
    """
    tajne = hadane_cislo(0, 10, 4)
    if tajne[0] == 0:
        tajne = hadane_cislo(0, 10, 4)

    str_tajne = [str(x) for x in tajne]
    tajne_cislo = int("".join(str_tajne))

    pocet_tipu = 0
    while True:
        tip = tipuj()
        list_tip = [int(x) for x in tip]

        bulls = kolik_bulls(list_tip, tajne)
        cows = kolik_cows(list_tip, tajne)

        vyhodnoceni_bulls(bulls, tajne_cislo)
        vyhodnoceni_cows(cows)

        pocet_tipu += 1
        print(f"Počet tipů je {pocet_tipu}")
        print(oddelovac)

if __name__ == "__main__":
    uvodni_text()
    hra()
