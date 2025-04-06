from game import Game
if __name__ == "__main__":
    game = Game()
    game.start()

    while game.is_running:
        game.update()

