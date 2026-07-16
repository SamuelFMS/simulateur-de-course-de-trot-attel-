import utils

# Constante vitesse selon la vitesse courante et le dé tiré
speed_by_current_horse_speed_and_dice = {0: [0, 1, 1, 1, 2, 2],
           1: [0, 0, 1, 1, 1, 2],
           2: [0, 0, 1, 1, 1, 2],
           3: [-1, 0, 0, 1, 1, 1],
           4: [-1, 0, 0, 0, 1, 1],
           5: [-2, -1, 0, 0, 0, 1],
           6: [-2, -1, 0, 0, 0, None], }

# distance/t selon la vitesse du cheval
speed_horse_meters = [0, 23, 46, 69, 92, 115, 138]

class Horse:
    def __init__(self, number:int, distance:int=0, speed:int|None=0) -> None:
        self.number = number
        self.distance = distance
        self.speed = speed

    def update_speed(self) -> None:
        if not self.speed is None:
            dice_result = utils.rollADiche()
            if speed_by_current_horse_speed_and_dice[self.speed][dice_result-1] is None:
                self.speed = None
            else:
                self.speed += speed_by_current_horse_speed_and_dice[self.speed][dice_result-1]

    def update_distance(self) -> None:
        if not self.speed is None:
            self.distance += speed_horse_meters[self.speed]

    def is_disqualified(self) -> bool:
        return self.speed is None

    def getDistance(self)->int:
        return self.distance

    def getNumber(self)->int:
        return self.number

    def getSpeed(self):
        return self.speed