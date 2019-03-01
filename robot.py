import field
import pygame
import window as win
import driver_station as ds


# robot x and y cord, from center of robot not top left
x = field.RED_2[0]
y = field.RED_2[1]


def draw():
    """Draw robot to screen"""
    pygame.draw.rect(win.screen, (0, 0, 0), [x - 20, y - 20, 40, 40], 0)


def drive():

    # use global x and y
    global x, y

    # update keyboard arrows
    ds.check_keyboard()

    # print of anything is pressed
    if ds.UP_PRESSED:
        print("Up arrow pressed")
        x += 1
    if ds.DOWN_PRESSED:
        print("Down arrow pressed")
        x -= 1
    if ds.LEFT_PRESSED:
        print("Left arrow pressed")
        y -= 1
    if ds.RIGHT_PRESSED:
        print("Right arrow pressed")
        y += 1
