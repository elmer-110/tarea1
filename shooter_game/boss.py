from shooter_game.opponent import Opponent

class Boss(Opponent):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def move(self):
        pass

    def shoot(self):
        pass

    def special_attack(self):
        pass
