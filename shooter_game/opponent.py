from shooter_game.character import Character

class Opponent(Character):
    def __init__(self, x, y, image):
        super().__init__(x, y, image, lives=1)
        self.is_star = False

    def move(self):
        pass

    def shoot(self):
        pass
