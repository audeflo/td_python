import re

class Customer:
    customers=[]
    def __init__(self, code, name, phone, address, email, solde):
        self.code   = code
        self.name   = name
        self.phone  = phone
        self.address = address
        self.email  = email
        self.solde  = solde
    
    @staticmethod
    def is_valid_code(code):
        return code.isalnum() and len(code) == 4

    @staticmethod
    def is_valid_name(name):
            return name.isalpha()
    
    @staticmethod
    def is_valid_phone(phone):
        pattern = r'^\d{8,10}$'
        return re.match(pattern, phone) is not None

    @staticmethod
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def menu_update():
        print("""
            1- code
            2- nom
            3- numéro de téléphone
            4- adresse
            5- email
            6- Retour""")
        
        number= input("Que voulez vous modifier:")
        while not (number.isdigit() and int(number) in range(1,7)):
            print("Incorrect. Veuillez saisir un nombre entre 1 et 6")
            number= input("Que voulez vous modifier:")
        number=int(number)
        return number
    
    @classmethod
    def add_customer(cls):
        code= input("Entrer votre code: ")
        while not cls.is_valid_code(code):
            print("Votre code doit avoir 4 caractères.")
            code= input("Entrer votre code: ")
          
        name= input("Entrer votre nom: ")
        while not cls.is_valid_name(name):
            print("Votre nom ne peut contenir que des lettres alphabétiques.")
            name= input("Entrer votre nom: ")
        
        phone= input("Entrer votre numéro de téléphone: ")
        while not cls.is_valid_phone(phone):
            print("Votre numéro de téléphone ne peut contenir que 8 à 10 chiffres. ")
            phone= input("Entrer votre numéro de téléphone: ")

        address= input("entrer votre adresse: ")
        
        email= input("Entrer votre email: ")
        while not cls.is_valid_email(email):
            print("Veuillez entrer une adresse valide.")
            email= input("Entrer votre email: ")

        new_customer = {
            "code": code,
            "name": name,
            "phone": phone,
            "address": address,
            "email": email,
            "solde": 0}

        cls.customers.append(new_customer)
        
        print(f"le client {name} a bien été ajouté !")

    @classmethod
    def remove_customer(cls):
        code= input("Entrer le code du client à supprimer: ")
        name=input("Entrer le nom du client à supprimer: ")
        for customer in cls.customers:
            if (customer["code"]==code and customer["name"]==name):
                cls.customers.remove(customer)
                print("Le client a bien été supprimé.")
            else: 
                print("Le client n'existe pas.")
    
    @classmethod
    def update_customer(cls):
        code= input("Entrer le code du client à modifier: ")
        name=input("Entrer le nom du client à modifier: ")
        for customer in cls.customers:
            if (customer["code"]==code and customer["name"]==name):
                to_update= cls.menu_update()
               #code
                if to_update==1:
                    new_code= input("Entrer votre nouveau code: ")
                    while not cls.is_valid_code(code):
                        print("Votre code doit avoir 4 caractères.")
                        new_code= input("Entrer votre code: ")
                    customer["code"]=new_code
               #nom
                elif to_update==2:
                    new_name= input("Entrer votre nouveau nom: ")
                    while not cls.is_valid_name():
                        print("Votre nom ne peut contenir que des lettres alphabétiques.")
                        new_name= input("Entrer votre nom: ")
                    customer["name"]=new_name
                #phone
                elif to_update==3:
                    new_phone= input("Entrer votre nouveau numéro de téléphone: ")
                    while not cls.is_valid_phone():
                        print("Votre numéro de téléphone ne peut contenir que 8 à 10 chiffres. ")
                        new_phone= input("Entrer votre nouveau numéro de téléphone: ")
                    customer["phone"]=new_phone

                #address
                elif to_update==4:
                    new_address= input("entrer votre nouvelle adresse: ")
                    customer["address"]=new_address
                
                #email
                else :
                    new_email= input("entrer votre nouvelle adresse mail: ")
                    while not cls.is_valid_email():
                        print("Veuillez entrer une adresse valide.")
                        new_email= input("entrer votre nouvelle adresse mail: ")
                    customer["email"]=new_email
            
            print(f"Les informations du client {name} ont été mises à jour.")
            return

        print(f"Aucun client trouvé avec le code {code} et le nom {name}. Veuillez réessayer.")

    @classmethod
    def display_customer(cls):
        if cls.customers:
            for customer in cls.customers:
                print(f"""
                    code: {customer["code"]}
                    nom: {customer["name"]}
                    numéro de téléphone: {customer["phone"]}
                    adresse: {customer["address"]}
                    email: {customer["email"]}
                    solde: {customer["solde"]} FCFA""")
        else:
            print("Il n'y a aucun client enregistré.")

    @classmethod
    def display_solde(cls):
        code= input("Entrer le code du client: ")
        name=input("Entrer le nom du client: ")
        for customer in cls.customers:
            if (customer["code"]==code and customer["name"]==name):
                print(f"Le solde du client {name} est de {customer['solde']} FCFA.")
            else: 
                print("Le client n'existe pas.")
            break