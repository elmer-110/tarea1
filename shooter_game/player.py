from shooter_game.character import Character

class Player(Character):
    def __init__(self, x, y, image):
        super().__init__(x, y, image, lives=3)
        self.score = 0

    def move(self):
        pass

    def shoot(self):
        pass
