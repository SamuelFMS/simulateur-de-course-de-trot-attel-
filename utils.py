import random


"""
    variables permettant de changer de couleur lors des prints
"""
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

"""
    methode permettant d'avoir un nombre entier aléatoire entre min et max
    :param min
    :param max
    :return int
"""
def rollADiche(min = 1, max = 6):
    return random.randint(min, max)


"""
    methode permetant la saisie d'un nombre attends un numero entier positif ou négatif
    :param message (La chaine a afficher a l'utilisateur pour la saisie)
    :param errorMessage (La chaine a afficher lors d'une erreur de saisie)
    :return retourne le nombre saisie par l'utilisateur
"""
def askNumber(message = None, erroMessage = None):
    while True:
        number = input("Entrer un numero: " if message is None else message)
        if number.lstrip("-").isdigit():
            return int(number)
        else:
            print("Incorrect input" if erroMessage is None else erroMessage)

"""
    méthode permetant la saisie avec une méthode passer en parametre pour verifier la saisie
    :param Condition (méthode permettant de verifier si la saisie est correcte)
    :param message (La chaine a afficher a l'utilisateur pour la saisie)
    :param erroMessage (La chaine a afficher lors dune erreur de saisie)
    :return saisi (L'input)
"""
def askCondition(Condition, message = None, erroMessage = None):
    while True:
        saisi = input("Entrer: " if message is None else message)
        if(Condition(saisi)):
            return saisi
        else:
            print("Incorrect input" if erroMessage is None else erroMessage)


"""
    méthode permettant la verification d'une chaine en nombre
    :param chaine (la chaine que l'on veut verifier)
    :return boolean
"""
def isANumber(chaine):
    if chaine.lstrip("-").isdigit():
        return True
    return False

if __name__ == '__main__':
    print(rollADiche())