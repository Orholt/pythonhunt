from random import randint, randrange
import pygame

if __name__ == "__main__":
    # setup
    pygame.init()
    pygame.display.set_caption("Python Hunt")
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    # assets initialization
    bg = pygame.image.load("Assets/Sprites/title_screen.png")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(bg, (0, 0))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
