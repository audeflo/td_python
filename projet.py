from customer import Customer
from transaction import Transaction

def menu_principal():
    print("""Choisissez parmi les 3 options suivantes:
    1- Gestion des clients
    2- Gestion des transactions
    3- Sortir""")
    choice= input("Quel est votre choix ----> ")
    while not (choice.isdigit() and int(choice) in range (1,4)):
        print("La valeur entrée est incorrecte. Veuillez choisir un nombre entre 1 et 3.")
        choice= input("Quel est votre choix ----> ")
    choice=int(choice)
    return choice 

def menu_client():
    print("""Gestion des clients:
    1- Afficher la liste des clients
    2- Ajouter un client
    3- Supprimer un client
    4- Modifier les informations du client
    5- Afficher le solde du client
    6- Retour""")
    choice= input("Quel est votre choix ----> ")
    while not (choice.isdigit() and int(choice) in range (1,7)):
        print("La valeur entrée est incorrecte. Veuillez choisir un nombre entre 1 et 6.")
        choice= input("Quel est votre choix ----> ")
    choice=int(choice)
    return choice 

def menu_transaction():
    print("""Gestion des transactions:
    1- Afficher toutes les transactions
    2- Afficher les transactions d'un client
    3- Faire un dépôt sur son compte
    4- Ajouter une transaction entre deux clients
    5- Modifier le solde d'un client
    6- Retour""")
    choice= input("Quel est votre choix ----> ")
    while not (choice.isdigit() and int(choice) in range (1,7)):
        print("La valeur entrée est incorrecte. Veuillez choisir un nombre entre 1 et 5.")
        choice= input("Quel est votre choix ----> ")
    choice=int(choice)
    return choice 

def exit_programm():    
    print("Fin du programme")
    exit()

while True:
    choice=menu_principal()
    if choice==1:
        while True:

            number= menu_client()
            if number==1:
                Customer.display_customer()
            elif number==2:
                Customer.add_customer()
            elif number==3:
                Customer.remove_customer()
            elif number==4:
                Customer.update_customer()
            elif number==5:
                Customer.display_solde()
            else:
                break
    elif choice==2:
        while True:
            number= menu_transaction()
            if number==1:
                Transaction.display_transaction()
            elif number==2:
                Transaction.transaction_by_customer()
            elif number==3:
                Transaction.make_deposit()
            elif number==4:
                Transaction.transaction_between_customers()
            elif number==5:
                Transaction.update_solde()
            else:
                break
    else:
        exit_programm()
