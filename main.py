import pygame
from player import Player
from constants import *


def main():
    pygame.init
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill("black")
        updatables.update(dt)
        for sprite in drawables:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000   # Limit to 60 FPS

    

    

if __name__ == "__main__":
    main()
 