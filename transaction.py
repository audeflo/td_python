from customer import Customer
from datetime import datetime
import uuid

class Transaction:
    transactions=[]
    transaction_canal=["Orange Money", "Wave", "Free Money"]

    def __init__(self, ref_paiement, date, amount, canal, client_code,transaction_type, receiver_phone):
        self.ref_paiement     = ref_paiement
        self.date             = date
        self.amount           = amount
        self.canal            = canal
        self.client_code      = client_code
        self.transaction_type = transaction_type
        self.receiver_phone   = receiver_phone
        self.updated          = False
    
    @staticmethod
    def is_valid_amount(amount):
        return amount.isdigit() 

    @staticmethod
    def menu_canal():
        print(""" Mode de transaction: 
            1- Orange Money
            2- Wave
            3- Free Money""")
        
        number= input("Quel est votre choix : ")
        while not (number.isdigit() and int(number) in range(1,4)):
            print("Incorrect. Veuillez saisir un nombre entre 1 et 3")
            number= input("Quel est votre choix : ")
        number=int(number)
        return Transaction.transaction_canal[number - 1]
    
    @staticmethod
    def menu_update():
        print("""
            1- référence de paiement
            2- date
            3- montant
            4- moyen de paiement
            5- client
            6- Retour""")
        
        number= input("Que voulez vous modifier:")
        while not (number.isdigit() and int(number) in range(1,7)):
            print("Incorrect. Veuillez saisir un nombre entre 1 et 6")
            number= input("Que voulez vous modifier:")
        number=int(number)
        return number
    
    # afficher toutes les transactions
    @classmethod
    def display_transaction(cls):
        if cls.transactions:
            for transaction in cls.transactions:
                client_name = next((customer["name"] for customer in Customer.customers if customer["code"] == transaction["client_code"]), "Client inconnu")
                print(f"""
                    Référence du paiement: {transaction["ref_paiement"]}
                    Date: {transaction["date"]}
                    Montant de la transaction: {transaction["amount"]}
                    Moyen de la transaction: {transaction["canal"]}
                    Client: {client_name}""")
        else:
            print("Il n'y a aucune transaction.")


    # afficher toutes les transactions d'un client
    @classmethod
    
    def transaction_by_customer(cls):
        code=input("Entrer le code du client: ")
        name=input("Entrer le nom du client: ")
        customer_found = False
        for customer in Customer.customers:
            if customer["code"] == code and customer["name"] == name:
                customer_found = True
                found_transactions = False
                for transaction in cls.transactions:
                    if transaction["client_code"] == code:
                        found_transactions = True
                        print(f"""
                            Référence du paiement: {transaction["ref_paiement"]}
                            Date: {transaction["date"]}
                            Montant de la transaction: {transaction["amount"]}
                            Moyen de la transaction: {transaction["canal"]}
                            Client: {name}""")
                        
                if not found_transactions:
                    print("Ce client n'a pas de transaction.")
                break
        if not customer_found:
            print("Ce client n'existe pas.") 
    
    
        # code= input("Entrer le code du client: ")
        # name= input("Entrer le nom du client: ")
        # for customer in Customer.customers:
        #     if customer["code"]==code and customer["name"]==name:    
        #         ref_paiement = str(uuid.uuid4()) 
        #         date=datetime.now().strftime("%Y-%m-%d")
        #         amount= input("Entrer le montant de la transaction: ")
        #         while not cls.is_valid_amount():
        #             print("Le montant doit être composé uniquement de chiffres.")
        #             amount= input("Entrer le montant de la transaction: ")

        #         canal= cls.menu_canal()

        #         new_transaction = {
        #             "ref_paiement"    : ref_paiement,
        #             "date"            : date,
        #             "amount"          : amount,
        #             "canal"           : canal,
        #             "client_code"     : customer["code"],
        #             "transaction_type": "Dépôt"}
                
        #         cls.transactions.append(new_transaction)
        
        #         print(f"la transaction du client {customer[name]} a bien été ajoutée !")
        #     else:
        #         print("Le client avec ces références n'existe pas.")
    
    
    # faire un dépôt sur son compte
    @classmethod
    def make_deposit(cls):
        code= input("Entrer le code du client: ")
        name= input("Entrer le nom du client: ")
        for customer in Customer.customers:
            if customer["code"]==code and customer["name"]==name:    
                ref_paiement = str(uuid.uuid4())

                amount= input("Entrer le montant de la transaction: ")
                while not cls.is_valid_amount(amount):
                    print("Le montant doit être composé uniquement de chiffres.")
                    amount= input("Entrer le montant de la transaction: ")
                
                date= datetime.now().strftime("%Y-%m-%d")
                canal= cls.menu_canal()
                
                new_transaction = {
                    "ref_paiement" : ref_paiement,
                    "date"         : date,
                    "amount"       : amount,
                    "canal"        : canal,
                    "client_code"  : customer["code"]}
                
                cls.transactions.append(new_transaction)
                print(f"la transaction du client {customer["name"]} a bien été ajoutée !")
                break
            else:
                print("Le client avec ces références n'existe pas.")

    # transaction entre deux clients
    @classmethod
    def transaction_between_customers(cls):
        sender_code = input("Entrer votre code client: ")
        sender_name = input("Entrer votre nom client : ")
        for sender in Customer.customers:
            if sender["code"] == sender_code and sender["name"] == sender_name:
                receiver_phone = input("Entrer le numéro du client destinataire: ")
                receiver = next((cust for cust in Customer.customers if cust["phone"] == receiver_phone), None)
                if receiver:
                    ref_paiement = str(uuid.uuid4())
                    amount = input("Entrer le montant de la transaction: ")
                    while not cls.is_valid_amount(amount):
                        print("Le montant doit être composé uniquement de chiffres.")
                        amount = input("Entrer le montant de la transaction: ")

                    if int(amount) > sender["solde"]:
                        print("Le solde de l'envoyeur est insuffisant pour effectuer cette transaction.")
                        return
                    date= datetime.now().strftime("%Y-%m-%d")
                    canal = cls.menu_canal()
                    
                    new_transaction = {
                    "ref_paiement"    : ref_paiement,
                    "date"            : date,
                    "amount"          : amount,
                    "canal"           : canal,
                    "client_code"     : sender_code,
                    "transaction_type":"Transaction entre clients",
                    "receiver_phone"  : receiver_phone}
                
                    cls.transactions.append(new_transaction)
                    print(f"La transaction entre les clients {sender['name']} et {receiver['name']} a bien été ajoutée !")
                    return
                else:
                    print("Le client destinataire avec ce code n'existe pas.")
                    return
            print("Le client envoyeur avec ces références n'existe pas.")

    @classmethod
    def update_solde(cls):
        code = input("Entrer votre code client: ")
        name = input("Entrer le nom du client à modifier: ")
        for customer in Customer.customers:
            if customer["code"] == code and customer["name"] == name:
                for transaction in cls.transactions:
                    if transaction.client_code == code and not transaction.updated:
                        receiver = next((cust for cust in Customer.customers if cust["code"] == transaction.receiver_phone), None)
                        if receiver:
                            if customer["solde"] >= int(transaction.amount):
                                customer["solde"] -= int(transaction.amount)
                                receiver["solde"] += int(transaction.amount)
                                transaction.updated = True
                                print(f"Le solde du client {customer['name']} a été débité et celui du destinataire {receiver['name']} a été crédité.")
                            else:
                                print(f"Le client {customer['name']} n'a pas suffisamment de solde pour effectuer cette transaction.")
                        else:
                            print("Le client destinataire n'existe pas.")
        print("Le client avec ces références n'existe pas ou la transaction a déjà été utilisée pour mettre à jour le solde.")