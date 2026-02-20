from circleshape import CircleShape
import pygame
import random
from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.rotation = 0
        self.rotation_speed = random.uniform(-1, 1)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rotation += self.rotation_speed * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)