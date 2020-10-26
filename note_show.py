import pygame
import os

import math


def draw(frame):

    os.environ['SDL_WINDOWID'] = str(frame.winfo_id())
    os.environ['SDL_VIDEODRIVER'] = 'windib'

    screen = pygame.display.set_mode((800, 500))
    screen.fill(pygame.Color(255, 255, 255))
    pygame.display.init()

    # pygame.draw.circle(screen, (0, 0, 0), (250, 250), 125)

    frame.update()

    return screen


def sinElips(screen, number):
    screen.fill((255, 255, 255))
    radius = math.sin(number / 60) * 50
    pygame.draw.circle(screen, (0, 0, 0), (200, 200), int(radius))
    pygame.display.update()


def drawLine(screen):

    pygame.draw.line(screen, (0, 0, 0), (0, 100), (800, 100))
    pygame.draw.line(screen, (0, 0, 0), (0, 150), (800, 150))

    pygame.draw.line(screen, (0, 0, 0), (0, 200), (800, 200))

    pygame.draw.line(screen, (0, 0, 0), (0, 250), (800, 250))
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (800, 300))
