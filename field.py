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

ROCKET_WIDTH = 38
ROCKET_HEIGHT = 40

# create a pygame rect to act as the cargo ship
# makes it easier to do collisions
cargo_ship = pygame.Rect(CARGO_X - CARGO_WIDTH // 2 + 3, CARGO_Y - CARGO_HEIGHT // 2, CARGO_WIDTH, CARGO_HEIGHT)

B1_X = 364
B1_Y = 40
b1 = pygame.Rect(B1_X - ROCKET_WIDTH // 2 + 3, B1_Y - ROCKET_HEIGHT // 2, ROCKET_WIDTH, ROCKET_HEIGHT)

R1_X = win.WIDTH - B1_X
R1_Y = 40
r1 = pygame.Rect(R1_X - ROCKET_WIDTH // 2 + 3, R1_Y - ROCKET_HEIGHT // 2, ROCKET_WIDTH, ROCKET_HEIGHT)

B2_X = 364
B2_Y = 490
b2 = pygame.Rect(B2_X - ROCKET_WIDTH // 2 + 3, B2_Y - ROCKET_HEIGHT // 2, ROCKET_WIDTH, ROCKET_HEIGHT)

R2_X = win.WIDTH - B1_X
R2_Y = 490
r2 = pygame.Rect(R2_X - ROCKET_WIDTH // 2 + 3, R2_Y - ROCKET_HEIGHT // 2, ROCKET_WIDTH, ROCKET_HEIGHT)

rockets = [b1, r1, b2, r2]


def draw_cargo_ship():
    """Draw cargo ship to the screen"""
    pygame.draw.rect(win.screen, (0, 0, 0), cargo_ship)


def draw_rockets():
    """Draw the rocket rects to the screen"""
    for rocket in rockets:
        pygame.draw.rect(win.screen, (0, 0, 0), rocket)

