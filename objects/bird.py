import os

import pygame.sprite

import assets
import settings
from layer import Layer
from objects.floor import Floor
from objects.pipe import Pipe


class Bird(pygame.sprite.Sprite):

    def __init__(self, *groups):
        self.path = os.path.join("assets", "audios")
        self._layer = Layer.PLAYER
        self.score = 0

        self.images = [
            assets.get_sprite("redbird-upflap"),
            assets.get_sprite("redbird-midflap"),
            assets.get_sprite("redbird-downflap")
        ]

        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(0, 50))

        self.mask = pygame.mask.from_surface(self.image)

        self.flap = 0

        self.passed_pipes = set()

        super().__init__(*groups)

    def update(self):
        self.images.insert(0, self.images.pop())
        self.image = self.images[0]

        self.flap += settings.GRAVITY
        self.rect.y += self.flap

        if self.rect.x < 50:
            self.rect.x += 3

    def handle_event(self, event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or \
                (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            self.flap = 0
            self.flap -= 6
            self.path = os.path.join("assets", "audios")
            flap_audio = pygame.mixer.Sound(os.path.join(self.path, "wing.wav"))

            flap_audio.play()

    def check_collision(self, sprites):
        for sprite in sprites:
            if (type(sprite) is Pipe or type(sprite) is Floor) and \
                    sprite.mask.overlap(self.mask, (self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y)) or \
                    self.rect.bottom < 0:
                return True
        return False

    def is_passed(self, sprites):
        for sprite in sprites:
            if type(sprite) is Pipe and sprite.rect.right < self.rect.left and sprite not in self.passed_pipes:
                self.passed_pipes.add(sprite)
                return True
        return False

    def get_score(self):
        return self.score
