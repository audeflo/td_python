def choice():
    number=input("Entrer un nombre:")
    while not number.isdigit():
        print("La valeur entrée est incorrecte. Veuillez réessayer.")
        number=input("Entrer un nombre:")
    number=int(number)
    return number


number=choice()

print(f"Les nombres entiers de 1 à {number} sont :")
for i in range(1, number + 1):
    print(i)


