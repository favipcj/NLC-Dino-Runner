import random
from nlc_dino_runner.component.obstacles.obstacle import Obstacle
from nlc_dino_runner.utils.constants import LARGE_CACTUS


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.index = random.randint(0, 2)
        self.image_cactus = LARGE_CACTUS[0]
        super().__init__(image, self.index)
        self.rect.y = 300
