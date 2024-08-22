from random import randint
from math import radians, cos, sin
from collections import namedtuple
from time import sleep

import pygame

LINES_AMOUNT = 1000000

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800

MIN_DISTANCE = 1
MAX_DISTANCE = 2

START_SLEEP_SECONDS = 3
BETWEEN_LINES_SLEEP_SECONDS = 0.000001

Point = namedtuple('Point', ['x', 'y'])

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


def generate_end_point(
    start_point: Point,
    distance: int | None = None,
    angel: int | None = None,
    logging: bool = False,
) -> Point:

    if not distance:
        distance = randint(MIN_DISTANCE, MAX_DISTANCE)
    if not angel:
        angel = randint(1, 360)

    # Angel in radians
    angel_radians = round(radians(angel), 4)

    # End point coordinates
    delta_x = round(distance * cos(angel_radians), 4)
    delta_y = round(distance * sin(angel_radians), 4)
    x2 = round(start_point.x + delta_x, 4)
    y2 = round(start_point.y + delta_y, 4)

    end_point = Point(x2, y2)

    if logging:
        print(f'{start_point} - distance={distance} - angel={angel} - {end_point}')

    return end_point


def wait_close():
    # Running flag
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def main():

    sleep(START_SLEEP_SECONDS)

    # Initialize Pygame
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("TestRandom")

    # Set start point
    start_point = Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

    # Clear the screen
    screen.fill(WHITE)

    counter = 1
    for i in range(LINES_AMOUNT):
        print(f'[{counter}] ', end='')
        end_point = generate_end_point(start_point, logging=True)
        pygame.draw.line(screen, BLACK, start_point, end_point, 2)
        if counter == 1:
            pygame.draw.circle(screen, BLUE, start_point, 5)
        else:
            pygame.draw.circle(screen, RED, start_point, 0)  # 2
        if counter == LINES_AMOUNT:
            pygame.draw.circle(screen, BLUE, end_point, 5)
        else:
            pygame.draw.circle(screen, GREEN, end_point, 0)  # 2
        # Update the display
        pygame.display.flip()
        start_point = end_point
        counter += 1
        sleep(BETWEEN_LINES_SLEEP_SECONDS)

    # Limit the frame rate to 60 frames per second
    pygame.time.Clock().tick(60)

    wait_close()


if __name__ == '__main__':
    main()


