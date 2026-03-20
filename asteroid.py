from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self,x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        new_vector = self.velocity.rotate(new_angle)
        new_vector2 = self.velocity.rotate(-new_angle)
        smaller_asteroids = self.radius - ASTEROID_MIN_RADIUS

        split1 = Asteroid(self.position.x, self.position.y, smaller_asteroids)
        split1.velocity = new_vector * 1.2
        split2 = Asteroid(self.position.x, self.position.y, smaller_asteroids)
        split2.velocity = new_vector2 * 1.2

        
        