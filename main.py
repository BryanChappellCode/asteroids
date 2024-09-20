import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    fps = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    continue_game = True

    while(continue_game):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for plyr in drawable:
            plyr.draw(screen)
        
        for plyr in updatable:
            plyr.update(dt)

        for aster in asteroids:
            if aster.collides(player):
                print("Game Over!")
                continue_game = False

            for bullet in shots:
                if bullet.collides(aster):
                    aster.kill()
                    bullet.kill()
                

        pygame.display.flip()

        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()


