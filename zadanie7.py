import random

pada = random.choice([True, False]) #Tutaj program losuje którąś z opcji
zgaduj = True
while zgaduj:
    odpowiedz = input("Czy pada? (t/n) ")
    if odpowiedz == "t" or "n":
        if odpowiedz == "t" and pada:
            print ("zgadles")
        else:
            print ("nie zgadles")
        break
