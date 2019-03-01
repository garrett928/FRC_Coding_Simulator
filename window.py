import pygame
import sys

background_image = pygame.image.load("game_field.jpg")
screen = pygame.display.set_mode((1017, 528))
print("starting screen")


def check_close():
    """check if window has requested to exit"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()


def init():
    """init game window and pygame"""
    # init pygame
    pygame.init()

    # set window title
    pygame.display.set_caption("Robot Sim")

    # flip to new display to refresh screen
    pygame.display.flip()


def draw_bg():
    """Draw the fields background image"""
    screen.blit(background_image, [0, 0])


def flip():
    """Flip the pygame window to a new frame"""
    pygame.display.flip()

