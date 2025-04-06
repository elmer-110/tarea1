from shooter_game.entity import Entity

class Character(Entity):
    def __init__(self, x, y, image, lives):
        super().__init__(x, y, image)
        self.lives = lives
        self.is_alive = True

    def move(self):
        pass

    def shoot(self):
        pass

    def collide(self, other):
        pass
