from toolkit import *
import pygame


WIDTH = 1200
HEIGHT = 900
RUNNING = True

SIDE = 600
K = 10

# WINDOW
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Guillotine problem algorithm visualisation')
screen = pygame.Surface((WIDTH, HEIGHT))
draw_area = pygame.Surface((SIDE, SIDE))
draw_area.fill((255, 255, 255))
pygame.font.init()


def grid(area, k):
    unit = int(SIDE / k)
    for row in range(0, SIDE, unit):
        pygame.draw.line(area, (150, 150, 150), (row, 0), (row, SIDE))
    for line in range(0, SIDE, unit):
        pygame.draw.line(area, (150, 150, 150), (0, line), (SIDE, line))


while RUNNING:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            RUNNING = False

    grid(draw_area, K)
    screen.fill((150, 150, 200))
    screen.blit(draw_area, ((WIDTH-SIDE)/2, (HEIGHT-SIDE)/2))
    window.blit(screen, (0, 0))
    pygame.display.flip()
