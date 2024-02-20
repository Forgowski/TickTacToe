import pygame
from settings import WIN_WIDTH, WIN_HEIGHT
from game import Game

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH))
clock = pygame.time.Clock()
running = True

while running:
    game = Game(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    game.update()
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()