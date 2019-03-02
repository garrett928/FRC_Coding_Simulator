import pygame
import sys
import driver_station as ds

from button import Button

WIDTH = 1017
HEIGTH = 528

# create field background
background_img = pygame.image.load("game_field.jpg")
# create main screen
screen = pygame.display.set_mode((WIDTH, HEIGTH))
# set window title
pygame.display.set_caption("Robot Sim")

start_button = Button(screen, "start", 10, 10, 40, 20)

print("starting screen")


def check_close():
    """check if window has requested to exit"""
    keys = pygame.key.get_pressed()
    ctrl_held = keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and ctrl_held:
                pygame.display.quit()
                pygame.quit()
                sys.exit()


def check_buttons():
    if start_button.is_clicked():
        ds.robot_stop = False

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

