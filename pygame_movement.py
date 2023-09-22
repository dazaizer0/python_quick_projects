import pygame
import sys

pygame.init()

title = "G A M E"
screen_width = 720
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)

class Entity:
    def __init__(self, width, height, position: pygame.Vector2, speed):
        self.width = width
        self.height = height
        self.x = position.x
        self.y = position.y
        self.speed = speed

class Object:
    def __init__(self, object_type, position: pygame.Vector2):
        self.object_type = object_type
        self.position = position


player_position = pygame.Vector2(320, 10)
player = Entity(81, 24, player_position, 1)

v2_1 = pygame.Vector2(0, 360)
v2_2 = pygame.Vector2(720, 360)

running = True
while running:
    keys = pygame.key.get_pressed()

    if player.x > 0 and player.x < 620:
        if keys[pygame.K_LEFT]:
            player.x -= player.speed
        if keys[pygame.K_RIGHT]:
            player.x += player.speed
    else:
        if player.x == 620:
            player.x = 615
        else:
            player.x = 25
    print(f'x: {player.x}, y: {player.y}')

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 127, 65), (player.x, player.y, player.width, player.height))
    pygame.draw.line(screen, (255, 0, 0), v2_1, v2_2, 8)
    pygame.display.update()

pygame.quit()
sys.exit()

