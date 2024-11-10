jmeno = input("Zadejte jmeno: ")
vaha = int(input("Zadejte vahu: "))
vyska = float(input("Zadejte vysku v centimetrech: "))/100
bmi_cele = vaha/(vyska**2)

bmi = round(bmi_cele,2)

if bmi < 18.5 :
    print(jmeno, "tve BMI je ", bmi , " coz spada do kategorie Podvyziva")

elif bmi >= 18.5 and bmi <25 :
    print(jmeno, "tve BMI je ", bmi , " coz spada do kategorie Zdrava vaha")

elif bmi >= 25 and bmi < 30:
    print(jmeno, "tve BMI je ", bmi , " coz spada do kategorie Mirna nadvaha")

elif bmi >= 30 and bmi < 40:
    print(jmeno, "tve BMI je ", bmi , " coz spada do kategorie Obezita")

else:
     print(jmeno, "tve BMI je ", bmi , " coz spada do kategorie Tezka obezita")



print(jmeno)
print(vaha)
print(vyska)
print(bmi)