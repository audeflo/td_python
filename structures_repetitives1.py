#10 premiers nombres pairs
def pairs():
    print("Les 10 premiers nombres pairs sont: ")

    for i in range(2,21):
        if i % 2==0:
            print(i)

#10 premiers nombres impairs
def impairs():

    print("Les 10 premiers nombres impairs sont :")
    count = 0
    number = 1
    while count < 10:
        if number % 2 != 0:
            print(number)
            count += 1
        number += 1

pairs()
impairs()
