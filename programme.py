import utils

if __name__ == '__main__':
    speedPerDiceRoll = {0: [0,1,1,1,2,2],
                        1: [0,0,1,1,1,2],
                        2: [0,0,1,1,1,2],
                        3: [-1,0,0,1,1,1],
                        4: [-1,0,0,0,1,1],
                        5: [-2,-1,0,0,0,1],
                        6:[-2,-1,0,0,0,"DQ"],}

    speed_horse = [0,23,46,69,92,115,138]
    numberOfHorse = 5
    current_speed_horse = [0]*numberOfHorse
    current_distance_horse = [0]*numberOfHorse

    while(True):
        #Effectuer un tour
        for x in range(numberOfHorse):
            if current_speed_horse[x] == "DQ":
                continue
            resultatDe = utils.rollADiche()
            currentSpeed = current_speed_horse[x]
            if speedPerDiceRoll[currentSpeed][resultatDe-1] == "DQ":
                current_speed_horse[x] = "DQ"
                continue
            newSpeed = currentSpeed + speedPerDiceRoll[currentSpeed][resultatDe-1]
            current_speed_horse[x] = newSpeed
            currentDistance = current_distance_horse[x] + speed_horse[newSpeed]
            current_distance_horse[x] = currentDistance
        print(current_speed_horse)
        print(current_distance_horse)
        input("Next? ")