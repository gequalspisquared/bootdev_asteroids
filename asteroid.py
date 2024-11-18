from circleshape import CircleShape
from constants import *

import pygame
import random

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.colordict.THECOLORS["white"], self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20.0, 50.0)
            new_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid1.velocity = self.velocity.rotate(random_angle)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid2.velocity = self.velocity.rotate(-random_angle)