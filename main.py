import pygame

import assets
import settings
from objects.UI import UI
from objects.background import Background
from objects.bird import Bird
from objects.floor import Floor
from objects.pipe import Pipe
from settings import *
from assets import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
create_pipe_event = pygame.USEREVENT
gameover = False
running = True
game_started = False
path = os.path.join("assets", "audios")

flap_audio = pygame.mixer.Sound(os.path.join(path, "wing.wav"))
point_audio = pygame.mixer.Sound(os.path.join(path, "point.wav"))
hit_audio = pygame.mixer.Sound(os.path.join(path, "hit.wav"))

assets.load_sprites()
sprites = pygame.sprite.LayeredUpdates()
start = UI.StartMessage(sprites)
Background(0, sprites)
Background(1, sprites)
Floor(0, sprites)
Floor(1, sprites)
score = UI.Score(sprites)

bird = Bird(sprites)

pygame.time.set_timer(create_pipe_event, 1500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_started:
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_started = True
                sprites.remove(start)
        if event.type == pygame.MOUSEBUTTONDOWN and gameover:
            gameover = False
            game_started = False
            sprites.empty()
            assets.load_sprites()
            start = UI.StartMessage(sprites)
            Background(0, sprites)
            Background(1, sprites)
            Floor(0, sprites)
            Floor(1, sprites)
            score = UI.Score(sprites)

            bird = Bird(sprites)
        else:
            if event.type == create_pipe_event:
                Pipe(sprites)

        bird.handle_event(event)

    screen.fill("pink")
    sprites.draw(screen)

    if not gameover and game_started:
        sprites.update()

    if bird.check_collision(sprites) and not gameover:
        gameover = True
        UI.Gameover(sprites)
        hit_audio.play()

    if bird.is_passed(sprites):
        score.value += 1
        point_audio.play()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
