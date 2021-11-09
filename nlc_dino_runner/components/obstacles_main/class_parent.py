from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):

    def __init__(self, image_list, index):
        self.unpacked_img = image_list[index]
        self.index = index
        self.rect = self.unpacked_img.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, img_list):
        self.rect.x -= 10
        if self.rect.x < -self.rect.width:
            img_list.pop()

    def draw(self, screen):
        screen.blit(self.unpacked_img, self.rect)
        # screen.blit(self.image_list[self.index], self.rect) # Where will be the y axis?
