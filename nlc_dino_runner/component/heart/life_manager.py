from nlc_dino_runner.utils.constants import numbers_life
from nlc_dino_runner.component.heart.life import Life


class LifeManager:
    def __init__(self):
        self.life = numbers_life
        #self.Life=Life()

    def update(self, game):
        #if game.player.dino_rect.colliderect(obstacle.rect):

        if self.life > 0:
            self.life -= 1
        else:
            game.playing = False

    def draw(self, screen):
        self.screen=screen
      #  for x in range(0, numbers_life):
            #Life.draw(self.screen)
            #Life.coordinates()

    def reset_obstacles(self):
        self.life
