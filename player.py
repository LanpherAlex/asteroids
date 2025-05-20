import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN
from shot import Shot



class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            direction = 1
            self.move(dt,direction)
        if keys[pygame.K_s]:
            direction = -1
            self.move(dt,direction)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        self.shoot_timer = max(0, self.shoot_timer - dt)

    def move(self,dt,direction):
        forward = pygame.Vector2(0 , 1).rotate(self.rotation)
        self.position += direction * forward * PLAYER_SPEED * dt

    def shoot(self,dt):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        forward = pygame.Vector2(0 , 1).rotate(self.rotation)
        velocity = forward * PLAYER_SHOOT_SPEED
        shot = Shot(self.position + forward * self.radius, velocity)


        
        
        
