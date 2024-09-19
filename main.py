import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps = pygame.time.Clock()
    dt = 0

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        player.draw(screen)
        player.update(dt)

        pygame.display.flip()

        

        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()


