import random

from circleshape import *
from constants import *
from logger import log_state, log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            asteroid_1_vel = self.velocity.rotate(random.uniform(20, 50))
            asteroid_2_vel = self.velocity.rotate(-random.uniform(20, 50))
            radius_new = self.radius - ASTEROID_MIN_RADIUS
            asteroid_new1 = Asteroid(self.position[0], self.position[1], radius_new)
            asteroid_new2 = Asteroid(self.position[0], self.position[1], radius_new)
            asteroid_new1.velocity = asteroid_1_vel * 1.2
            asteroid_new2.velocity = asteroid_2_vel * 1.2


