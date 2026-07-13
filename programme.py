import utils

def coursesTerminer(speedHorse, distanceHorse, distance_win):
    for x in range(number_horse):
        if(speedHorse[x] == "DQ"):
            continue
        if(distanceHorse[x] >= distance_win):
            continue
        return False
    return True

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

    while True:
        number_horse = utils.askNumber("Entrez le nombres de chevaux: ")
        if number_horse >= 15 and number_horse <= 20:
            break
        print("Nombre entre 15 et 20 attendus")
    distance_win = 2400

    current_speed_horse = [0] * number_horse
    current_distance_horse = [0] * number_horse
    classement_horse = [0] * number_horse
    nouveauclassement = 1

    while(True):
        if(coursesTerminer(current_speed_horse, current_distance_horse, distance_win)):
            break
        #Effectuer un tour
        newSpeed = 0
        currentDistance = 0

        classement = nouveauclassement
        for x in range(number_horse):
            if current_speed_horse[x] == "DQ":
                print(f"{x} -> Disqualifié")
                continue
            if(current_distance_horse[x] >= distance_win):
                print(f"{x} -> {classement_horse[x]}")
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
    print("======= Classement Finale =======")
    for x in range(number_horse):
        print(f"{x} -> {"Disqualifié" if classement_horse[x] == 0 else classement_horse[x]}")