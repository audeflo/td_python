def choice():
    grade= input ("Entrer votre note svp: ")
    while not (grade.replace('.', '', 1).isdigit() and 0 <= float(grade) <=20):
        print("La valeur entrée est incorrecte.")
        grade= input ("Entrer votre note svp: ")
    grade=float(grade)
    return grade

def remark(grade):
    if grade < 10:
        print("Echec")
    elif 10 <= grade < 12:
        print("Passable")
    elif 12<= grade < 14:
        print("Satisfaisant")
    elif 14<= grade < 16 :
        print("Bien")
    elif 16 <= grade < 18:
        print("Bien")
    else:
        print("Excellent")

grade=choice()
remark(grade)
