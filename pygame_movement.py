import pygame
import sys

pygame.init()

screen_width = 720
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("GAME")

class Entity:
    def __init__(self, width, height, speed):
        self.width = width
        self.height = height
        self.x = (width - width) // 2
        self.y = (height - height) // 2
        self.speed = speed


player = Entity(50, 50, 2)

running = True
while running:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player.speed
    if keys[pygame.K_RIGHT]:
        player.x += player.speed
    if keys[pygame.K_UP]:
        player.y -= player.speed
    if keys[pygame.K_DOWN]:
        player.y += player.speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 127, 65), (player.x, player.y, player.width, player.height))
    pygame.display.update()

pygame.quit()
sys.exit()