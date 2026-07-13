import random

def rollADiche(min = 1, max = 6):
    return random.randint(min, max)

def askNumber(message = None, erroMessage = None):
    while True:
        number = input("Entrer un numero: " if message is None else message)
        if number.lstrip("-").isdigit():
            return int(number)
        else:
            print("Incorrect input" if erroMessage is None else erroMessage)

def askCondition(Condition, message = None, erroMessage = None):
    while True:
        saisi = input("Entrer: " if message is None else message)
        if(Condition(saisi)):
            return saisi
        else:
            print("Incorrect input" if erroMessage is None else erroMessage)

def isANumber(chaine):
    if chaine.lstrip("-").isdigit():
        return True
    return False

if __name__ == '__main__':
    print(rollADiche())