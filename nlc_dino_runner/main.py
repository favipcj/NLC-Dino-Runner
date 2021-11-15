import pygame
from nlc_dino_runner.component.game import Game

if __name__ == "__main__":
    game = Game()
    print(pygame.font.get_fonts())
    game.execute()

print("hello world")


