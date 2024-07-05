panier=[]

#afficher le menu
def menu():
    print("""Choisissez parmi les 5 options suivantes:
    1- Ajouter un article dans le panier
    2- Supprimer un article du panier
    3- Afficher tous les articles
    4- Vider le panier
    5- Quitter""")

#verificaion du choix       
def choice():
    number=input("Quel est votre choix?: ")
    while not (number.isdigit() and int(number) in range(1,6)):
        print("La valeur entrée est incorrecte. Veuillez réessayer.")
        number=input("Quel est votre choix?: ")
    number=int(number)
    return number

#ajouter un article       
def add_article():
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

#supprimer un article
def delete_article():
    article=input("Entrer le nom de l'article: ")
    if panier:
        for i in panier:
            if i["name"]==article:
                panier.remove(i)
                print("Votre article a bien été supprimé.")
    else:
        print("Aucun article avec ce nom")

#afficher les articles
def display_article():
    if panier:
        for i in panier:
            print(f"""
                article: {i["name"]}
                prix: {i["prix"]} FCFA""")
    else:
        print("Votre panier est vide")
    
#supprimer tous les articles
def clear_all():    
    if panier:
        for i in panier:
            panier.clear()
            print("Votre panier est maintenant vide")
    else:
        print("Votre panier est déjà vide.")

#sortir du programme 
def exit_programm():    
    print("Fin du programme")
    exit()

while True:
    menu()
    number=choice()
    if number==1:
        add_article()
    elif number==2:
        delete_article()
    elif number==3:
        display_article()
    elif number==4:
        clear_all()
    elif number==5:
        exit_programm()