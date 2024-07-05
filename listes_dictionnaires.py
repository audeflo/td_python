menu=("""Choisissez parmi les 5 options suivantes:
    1- Ajouter un article dans le panier
    2- Supprimer un article du panier
    3- Afficher tous les articles
    4- Vider le panier
    5- Quitter""")

panier=[]

def choice():
    number=input("Quel est votre choix?: ")
    while not (number.isdigit() and int(number) in range(1,6)):
        print("La valeur entrée est incorrecte. Veuillez réessayer.")
        number=input("Quel est votre choix?: ")
    number=int(number)
    return number

def option(number):
    #option1
    if number==1:
        article=input("Entrer le nom de l'article: ")
        while not article.isalnum() :
            print("Le nom de l'article est incorrect.")
            article=input("Entrer le nom de l'article: ")

        price=input("Entrer le prix de l'article: ")
        while not price.isdigit():
            print("Le prix doit être composé uniquement de chiffres.")
            price=input("Entrer le prix de l'article: ")
        
        shop={"name":article,"prix":price}
        panier.append(shop)
        print("Votre article a bien été ajouté.")
    
    #option2
    elif number==2:
        article=input("Entrer le nom de l'article: ")
        if panier:
            for i in panier:
                if i["name"]==article:
                    panier.remove(i)
                    print("Votre article a bien été supprimé.")
        else:
            print("Aucun article avec ce nom")

    #option3
    elif number==3:
        if panier:
            for i in panier:
                print(f"""
                    article: {i["name"]}
                    prix: {i["prix"]} FCFA""")
        else:
            print("Votre panier est vide")
    
    #option4
    elif number==4:
        if panier:
            for i in panier:
                panier.clear()
                print("Votre panier est maintenant vide")
        else:
            print("Votre panier est déjà vide.")

    #option5
    elif number==5:
        print("Fin du programme")
        exit()

while True:
    print(menu)
    number=choice()
    option(number)