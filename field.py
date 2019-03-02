import robot
import pygame
import window as win

# Coordinates for x, y of red 2 alliance.
# Coordinates is given from the center
RED_2 = (130, 264)

X_PADDING = 40
Y_PADDING = 40

# x and y pos of cargo ship given from center of ship
CARGO_X = win.WIDTH // 2
CARGO_Y = win.HEIGTH // 2

# width and height of cargo shi[
CARGO_WIDTH = 295
CARGO_HEIGHT = 70

# create a pygame rect to act as the cargo ship
# makes it easier to do collisions
cargo_ship = pygame.Rect(CARGO_X - CARGO_WIDTH // 2 + 3, CARGO_Y - CARGO_HEIGHT // 2, CARGO_WIDTH, CARGO_HEIGHT)


def draw_cargo_ship():
    """Draw cargo ship to the screen"""
    pygame.draw.rect(win.screen, (0, 0, 0), cargo_ship)
