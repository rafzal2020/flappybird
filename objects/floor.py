import pygame.sprite

import assets
import settings
from layer import Layer


class Floor(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self._layer = Layer.FLOOR
        self.image = assets.get_sprite("floor")
        self.rect = self.image.get_rect(topleft=(settings.SCREEN_WIDTH * index, 400))
        self.mask = pygame.mask.from_surface(self.image)

        super().__init__(*groups)

    def update(self):
        self.rect.x -= 2

        if self.rect.right <= 0:
            self.rect.x = settings.SCREEN_WIDTH
