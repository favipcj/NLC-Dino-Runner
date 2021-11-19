import random
import time

from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HAMMER, SCREEN_HEIGHT, HAMMER_TYPE


class Hammer(Sprite):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_HEIGHT + random.randint(800, 1000)
        self.rect.y = random.randint(100, 120)
        self.rectx = 140
        self.recty = 320

    def update(self, game_speed, hammer):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            hammer.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def draw_hammer(self,screen,speed_hammer,press_space):

        if press_space==True:

            self.rectx +=speed_hammer

            screen.blit(self.image,[self.rectx,self.recty])
            speed_hammer +=1

        if 1000<self.rectx<=1100:

            self.rectx=120
            speed_hammer=20
            press_space=False

        return speed_hammer,press_space
