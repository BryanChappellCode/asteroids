from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):


    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        asteroid_shape = pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        angle_one = self.velocity.rotate(random_angle)
        angle_two = self.velocity.rotate(-1 * random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        aster_one = Asteroid(self.position.x, self.position.y, new_radius)
        aster_two = Asteroid(self.position.x, self.position.y, new_radius)

        aster_one.velocity = angle_one * 1.2
        aster_two.velocity = angle_two * 1.2
