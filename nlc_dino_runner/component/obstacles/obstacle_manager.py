import pygame.time


from nlc_dino_runner.utils.constants import SMALL_CACTUS, numbers_life
from nlc_dino_runner.component.obstacles.cactus import Cactus


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

      #  print("vidas",self.lifes)
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):

                if game.player.shield:
                    self.obstacles.remove(obstacle)
                elif game.lifes>0:
                    self.obstacles.remove(obstacle)
                    game.lifes -= 1
                    #print(game.lifes)

                else:

                    game.playing = False


                    game.death_count += 1

                    #print(game.lifes,game.death_count)
                    break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
