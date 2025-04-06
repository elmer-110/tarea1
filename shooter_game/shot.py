from shooter_game.entity import Entity

class Shot(Entity):
    def __init__(self, x, y, image, direction):
        super().__init__(x, y, image)
        self.direction = direction

    def move(self):
        pass

    def hit_target(self, target):
        pass
