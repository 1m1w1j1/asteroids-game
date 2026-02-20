import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print("Starting Asteroids with pygame version: ", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    fps_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    
    Player.containers = (updatable, drawable)


    Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        updatable.update(dt)
        
        for drawing in drawable:
            drawing.draw(screen)
        
        pygame.display.flip()
        
        dt = fps_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
