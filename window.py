import pygame
import sys

# create field background
background_img = pygame.image.load("game_field.jpg")
# create main screen
screen = pygame.display.set_mode((1017, 528))
# set window title
pygame.display.set_caption("Robot Sim")

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



    # flip to new display to refresh screen
    pygame.display.flip()


def draw_bg():
    """Draw the fields background image"""
    screen.blit(background_img, [0, 0])


def flip():
    """Flip the pygame window to a new frame"""
    pygame.display.flip()

