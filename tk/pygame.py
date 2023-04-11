import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((380, 250))
pygame.display.set_caption('Jogo foda')
clock = pygame.time.Clock()

sky = pygame.image.load('tk/back.png')
ground = pygame.image.load('tk/ground.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, -100))
    pygame.display.update()
    clock.tick(60)
