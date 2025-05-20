import pygame
from constants import *
import sys
from player import Player
from asteroid import Asteroid  # Change to singular
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.update(dt)
    player.rotation = 180

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    # AsteroidField only goes in updatable - not drawable
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()


    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                running = False
        for asteroid in asteroids:
            for shot in shots.sprites():
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)
         
    pygame.quit()
    sys.exit()
        
        



if __name__ == "__main__":
    main()