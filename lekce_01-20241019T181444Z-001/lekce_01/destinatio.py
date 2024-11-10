mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)

slevy = ("Olomouc", "Svitavy", "Ostrava")

domeny = ("gmail.com", "seznam.cz", "email.cz")

cara = "=" * 35
nabidka = """
1 - Praha   | 150,-Kč
2 - Viden   | 200,-Kč
3 - Olomouc | 120,-Kč
4 - Svitavy | 120,-Kč
5 - Zlin    | 100,-Kč
6 - Ostrava | 180,-Kč
"""

print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(cara)

print(nabidka)
print(cara)

destinace = int(input("CISLO DESTINACE: "))

if destinace <= 6:
    True
else:
    print("Destinace neexistuje")
    quit()


jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")

if jmeno.isalpha() and prijmeni.isalpha():
    print("Vase cele jmeno", jmeno, prijmeni)
    print("Krestni jmeno: ", jmeno)
else:
    print("Vase cele jmeno", jmeno, prijmeni)
    print("Neplatne jmeno!")
    quit()


rok = int(input("Zadejte rok narozeni: "))

vek = 2024 - rok

if vek >= 18:
    print("Pristup povolen...")
else:
    print("Jste prilis mlady na nakup jizdenek!")
    print("Ukoncuji program")
    quit()


email = input("E-MAIL: ")



if "@" in email and email.split("@")[1] in domeny:
    print("Jizdenku jsme odeslali na e-mail", email)
    print("Overeni e-mailu probehlo v poradku.")
else:
    print("Jizdenku jsme odeslali na e-mail", email)
    print("Tento e-mail je neplatny!")
    print("Ukoncuji program")
    quit()


print(cara)

cilova_stanice = mesta[int(destinace) - 1] # mesta[int(destinace) - 1


print(cilova_stanice)

if mesta[int(destinace) - 1] in slevy:
    finalni_cena = ceny[int(destinace) - 1]*0.75
    print("Ziskavate 25% slevu! Nova cena:", finalni_cena, ",-Kč")
else:
    finalni_cena = ceny[int(destinace) - 1]
    print("Jizdenka bez slevy. Cena: ", finalni_cena, ",-Kč")




print(cara)



print("Cilova destinace:", cilova_stanice)
