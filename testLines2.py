import pygame
import random
import math

pygame.init()
display_width = 800
display_height = 600

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("explore")


def branch(length, theta, start):
    if length > 5:
        xend = start[0] + (length * math.cos(math.radians(theta)))
        yend = start[1] + (length * math.sin(math.radians(theta)))
        pygame.draw.line(window, white, start, (xend, yend), 1)
        branch(0.75 * length, theta + 25, (xend, yend))
        branch(0.75 * length, theta - 25, (xend, yend))


def mainLoop():
    run = True
    theta = -90

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        window.fill(black)

        branch(100, theta, (400, 600))
        pygame.display.flip()


mainLoop()
pygame.quit()
