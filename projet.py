def menu_principal():
    print("""Choisissez parmi les 3 options suivantes:
    1- Gestion des clients
    2- Gestion des transations
    3- Sortir""")

def menu_client():
    print("""Gestion des clients:
    1- Afficher la liste des clients
    2- Ajouter un client
    3- Supprimer un client
    4- Modifier les informations du client
    5- Afficher le solde du client
    6- Retour""")

def menu_transaction():
    print("""Gestion des transactions:
    1- Afficher toutes les transactions
    2- Afficher les transactions d'un client
    3- Ajouter une transaction
    4- Modifier le solde d'un client
    5- Retour""")

class Client:
    customers=[]
    def __init__(self, code, name, phone, adress, email):
        self.code   = code
        self.name   = name
        self.phone  = phone
        self.adress = adress
        self.email  = email

    def add_customer():
        code= input("Entrer votre code: ")
        name= input("Entrer votre nom: ")
        while not name.isalpha():
            print("Veuillez entrer un nom valide.")
            name= input("Entrer votre nom: ")
        phone= input("Entrer votre numéro de téléphone: ")
        while not phone.isdigit():
            print("Veuillez entrer un numéro valide.")
            phone= input("Entrer votre numéro de téléphone: ")
        adress= input("entrer votre adresse: ")
        email= input("Entrer votre email: ")
        Client.code   = code
        Client.name   = name
        Client.phone  = phone
        Client.adress = adress
        Client.email  = email
        
        customer={"code":Client.code,"name":Client.name,"phone":Client.phone,"adress":Client.adress, "email":Client.email}
        Client.customers.append(customer)

