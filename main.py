import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps = pygame.time.Clock()
    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color="Black")
        pygame.display.flip()

        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()


