from shooter_game.player import Player
from shooter_game.opponent import Opponent

class Game:
    def __init__(self):
        self.score = 0
        self.player = Player(100, 400, "player.png")
        self.opponent = Opponent(100, 100, "enemy.png")
        self.is_running = False

    def start(self):
        self.is_running = True
        print("Game started")

    def update(self):
        pass  # Aquí va la lógica del juego

    def end_game(self):
        self.is_running = False
        print("Game over")
