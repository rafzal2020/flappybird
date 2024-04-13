import pygame.sprite

import assets
import settings
from layer import Layer
from objects.bird import Bird
from objects.pipe import Pipe


class UI(pygame.sprite.Sprite):
    class Score(pygame.sprite.Sprite):
        def __init__(self, *groups):
            self._layer = Layer.UI
            self.value = 0

            self.__create()

            self.image = pygame.surface.Surface((0, 0), pygame.SRCALPHA)

            super().__init__(*groups)

        def __create(self):
            self.str_value = str(self.value)

            self.images = []
            self.width = 0

            for str_value_char in self.str_value:
                img = assets.get_sprite(str_value_char)
                self.images.append(img)
                self.width += img.get_width()

            self.height = self.images[0].get_height()
            self.image = pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA)
            self.rect = self.image.get_rect(center=(settings.SCREEN_WIDTH / 2, 50))

            x = 0
            for img in self.images:
                self.image.blit(img, (x, 0))
                x += img.get_width()

        def update(self):
            self.__create()

    class Gameover(pygame.sprite.Sprite):
        def __init__(self, *groups):
            self._layer = Layer.UI
            self.image = assets.get_sprite("gameover")
            self.rect = self.image.get_rect(topleft=(50, 100))

            super().__init__(*groups)

    class StartMessage(pygame.sprite.Sprite):
        def __init__(self, *groups):
            self._layer = Layer.UI
            self.image = assets.get_sprite("message")
            self.rect = self.image.get_rect(topleft=(50, 100))

            super().__init__(*groups)








