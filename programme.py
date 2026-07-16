import utils
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
    :param speedHorse (Liste de vitesse de cheval pour savoir si DQ)
    :param distanceHorse (Quel distance a parcouru le cheval)
    :param distance_win  (distance pour remporter)
    :return boolean
"""
def coursesTerminer(speedHorse, distanceHorse, distance_win):
    for x in range(number_horse):
        if(speedHorse[x] == "DQ"):
            continue
        if(distanceHorse[x] >= distance_win):
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

if __name__ == '__main__':
    speed_per_dice_roll = {0: [0, 1, 1, 1, 2, 2],
                           1: [0,0,1,1,1,2],
                           2: [0,0,1,1,1,2],
                           3: [-1,0,0,1,1,1],
                           4: [-1,0,0,0,1,1],
                           5: [-2,-1,0,0,0,1],
                           6:[-2,-1,0,0,0,"DQ"], }

    speed_horse = [0,23,46,69,92,115,138]

    distance_win = 2400
    nouveauclassement = 1

    #Nombre de cheval
    while True:
        number_horse = utils.askNumber("Entrez le nombres de chevaux: ")
        if number_horse >= 12 and number_horse <= 20:
            break
        print("Nombre entre 12 et 20 attendus")

    #Type de course

    saisiTypeDeCourse = utils.askCondition(verifSaisieTypeRace, "Voulez vous faire un tiercé (A) ou un quatré (B) ou un quinté (C)")
    type_race = TypeRace.Tierce if saisiTypeDeCourse == "A" else TypeRace.Quatre if saisiTypeDeCourse == "B" else TypeRace.Quinte
    print(type_race)

    current_speed_horse = [0] * number_horse
    current_distance_horse = [0] * number_horse
    classement_horse = [0] * number_horse
    nombreTour = 0
    while(True):
        if(coursesTerminer(current_speed_horse, current_distance_horse, distance_win)):
            break
        nombreTour += 1
        print(f"Tour {nombreTour}")
        #Effectuer un tour
        newSpeed = 0
        currentDistance = 0

        classement = nouveauclassement
        for x in range(number_horse):
            if current_speed_horse[x] == "DQ":
                print(f"{utils.RED}{x} -> Disqualifié{utils.RESET}")
                continue
            if(current_distance_horse[x] >= distance_win):
                print(f"{utils.GREEN}{x} -> Position {classement_horse[x]}{utils.RESET}")
                continue
            print(f"{x} -> {afficher_barre_de_progression(current_distance_horse[x], distance_win)} ({current_distance_horse[x]}/{distance_win}) vitesse: {current_speed_horse[x]}")
            resultatDe = utils.rollADiche()
            currentSpeed = current_speed_horse[x]
            if speed_per_dice_roll[currentSpeed][resultatDe - 1] == "DQ":
                print("Disqualifié")
                current_speed_horse[x] = "DQ"
                continue
            newSpeed = currentSpeed + speed_per_dice_roll[currentSpeed][resultatDe - 1]
            current_speed_horse[x] = newSpeed
            currentDistance = current_distance_horse[x] + speed_horse[newSpeed]
            current_distance_horse[x] = currentDistance
            if (current_distance_horse[x] >= distance_win):
                classement_horse[x] = classement
                nouveauclassement+=1

        input("Next? ")
        print("\n")

    print("\n")
    print("======= Classement Finale =======")
    nombre_a_afficher = type_race.value
    for pos in range(nombre_a_afficher):
        res = []
        for x in range(number_horse):
            if(classement_horse[x] == pos+1):
                res.append(x)
        resString = ""
        if len(res) != 0:
            for t in res:
                resString += "Cheval " + str(t) + " "
            print(f"En position {pos+1} : {resString}")


