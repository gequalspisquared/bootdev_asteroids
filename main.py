from constants import *

import pygame

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    (init_numpass, init_numfail) = pygame.init()
    print(f"pygame init: {init_numpass} passed, {init_numfail} failed")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw the screen
        screen.fill(pygame.Color(0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
