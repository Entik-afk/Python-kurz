mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
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
# Vypiš nabídku cílových destinací a odděl ji pomocnou proměnnou 'cara'
print(nabidka)  # promennna 'nabidka' je napsana tak, za zacina prazdnym radkem.
print(cara) 

jmeno = input("Zadejte sve jmeno:")
prijmeni = input("Zadejte sve prijmeni:")
cislo_destinace = int(input("Zadejte cislo destinace kde jedete:"))
email = input("Zadejte prosim svuj email:")

#print("Cislo destinace: ", cislo_destinace)
#print("Jmeno: ", jmeno)
#print("Prijmeni: ", prijmeni)
#print("EMAIL: ", email)

print(cara)

cilovka = mesta[cislo_destinace - 1]
cena_final = ceny[cislo_destinace - 1]

print(cilovka)
print(cena_final, "Kc")

print(cara)
print("Cestujici:", jmeno, "", prijmeni)
print("Cilova destinace: ", cilovka)
print("Cena jizdneho: ", cena_final, ",Kc")
print("Jizdenku jsme odeslali na email: ", email)