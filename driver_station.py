import pygame


# flag to keep track of if robot code should run in infinite loop or not
robot_stop = False



UP_PRESSED = False
DOWN_PRESSED = False
LEFT_PRESSED = False
RIGHT_PRESSED = False


def check_keyboard():
    """Check and update the keyboard state"""

    # use global vars to update
    global UP_PRESSED
    global DOWN_PRESSED
    global LEFT_PRESSED
    global RIGHT_PRESSED

    # get all pressed keys on the keyboard
    key = pygame.key.get_pressed()

    # update global vars
    UP_PRESSED = key[pygame.K_UP]
    DOWN_PRESSED = key[pygame.K_DOWN]
    LEFT_PRESSED = key[pygame.K_LEFT]
    RIGHT_PRESSED = key[pygame.K_RIGHT]

