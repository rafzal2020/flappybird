import os
import pygame

sprites = {}

music = {}


def load_sprites():
    path = os.path.join("assets", "sprites")
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))


def load_music():
    path = os.path.join("assets", "audios")
    for file in os.listdir(path):
        music[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))


def get_sprite(name):
    return sprites[name]
