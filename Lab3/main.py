# Pygame шаблон - скелет для нового проекта Pygame
import pygame
from random import randint

WIDTH = 360
HEIGHT = 480
FPS = 30

x = 50
y = 50
width = 30
height = 30
speed = 5

pygame.image.load('tile/tile.png')

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < WIDTH - width:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < HEIGHT - height:
        y += speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), (x, y, width, height))
    pygame.display.update()

pygame.quit()
