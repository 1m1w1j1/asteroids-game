import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state



def main():
    print("Starting Asteroids with pygame version: ", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    fps_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        fps_clock.tick(60) 
        dt = fps_clock.get_time() / 1000.0
        #print("dt: ", dt)

    screen.fill("black")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.draw(screen)
    pygame.display.flip()


if __name__ == "__main__":
    main()
