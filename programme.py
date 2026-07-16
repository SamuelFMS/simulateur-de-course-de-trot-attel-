from array import ArrayType

import utils
import Horse
from enum import Enum

"""
    Création d'un enum pour le type de course tierce, quatre, quinte
"""
class TypeRace(Enum):
    Tierce = 3
    Quatre = 4
    Quinte = 5

"""
    méthode permettant de verifier si une course est terminer
    :param horse (Liste de class Horse) 
    :param distance_win  (distance pour remporter)
    :return boolean
"""
def coursesTerminer(horses, distance_win):
    for horse in horses:
        if horse.is_disqualified():
            continue
        if horse.getDistance() >= distance_win:
            continue
        return False
    return True


"""
    méthode permettant de verifier si la chaine saisie est A ou B ou C
    :param saisie
    :return boolean
"""
def verifSaisieTypeRace(saisie):
    if saisie == "A" or (saisie == "B" or saisie == "C"):
        return True
    return False

"""
    méthode permettant de retourne une barre de progression du cheval en un string
    :param distance
    :param maxDistance 
    :return chaine 
"""
def afficher_barre_de_progression(distance, maxDistance):
    taille_char = 40
    v = distance / maxDistance
    c = min(taille_char, int(taille_char * v))
    x = taille_char - c
    return ((c*"=") + (x*"-"))

"""
    méthode permettant de retourne la position du cheval dans le classement
    :param classemet (liste de cheval)
    :param horse
    :return int 
"""
def getPositionInClassement(classement, horse):
    for x in range(len(classement)):
        if horse.getNumber() == classement[x].getNumber():
            return x
    return None
if __name__ == '__main__':
    distance_win = 2400

    #Nombre de cheval
    while True:
        number_horse = utils.askNumber("Entrez le nombres de chevaux: ")
        if number_horse >= 12 and number_horse <= 20:
            break
        print("Nombre entre 12 et 20 attendus")

    # Initialisation des cheveaux
    list_horse = []
    for x in range(number_horse):
        list_horse.append(Horse.Horse(int(x)))
    classement_horse = []

    #Type de course
    saisiTypeDeCourse = utils.askCondition(verifSaisieTypeRace, "Voulez vous faire un tiercé (A) ou un quatré (B) ou un quinté (C)")
    type_race = TypeRace.Tierce if saisiTypeDeCourse == "A" else TypeRace.Quatre if saisiTypeDeCourse == "B" else TypeRace.Quinte

    nombreTour = 0
    while not coursesTerminer(list_horse, distance_win):
        # Effectuer un tour
        nombreTour += 1
        print(f"Tour {nombreTour}")
        finished_horse_round = []
        for horse in list_horse:
            # Affichage parcours pour chaque cheval
            if horse.is_disqualified():
                print(f"{utils.RED}{horse.getNumber()} -> Disqualifié{utils.RESET}")
                continue
            if(horse.getDistance() >= distance_win):
                print(f"{utils.GREEN}{horse.getNumber()} -> Position {getPositionInClassement(classement_horse, horse)}{utils.RESET}")
                continue
            print(f"{horse.getNumber()} -> {afficher_barre_de_progression(horse.getDistance(), distance_win)} ({horse.getDistance()}/{distance_win}) vitesse: {horse.getSpeed()}")

            # Avancer
            horse.update_speed()
            horse.update_distance()
            if horse.getDistance() >= distance_win:
                classement_horse.append(horse)

        input("Next? ")
        print("\n")

    print("\n")
    print("======= Classement Finale =======")
    nombre_a_afficher = type_race.value
    for pos in range(nombre_a_afficher):
        print(f"En {pos+1}{"ere" if pos==0 else "eme"} place : Cheval n°{classement_horse[pos].getNumber()}")


