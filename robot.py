import field
import pygame
import math
import window as win
import driver_station as ds


# robot x and y cord, from center of robot not top left
x = field.RED_2[0]
y = field.RED_2[1]

# field heading, keep track of robot angle
theta = 0
delta_theta = 0

# robot width and height
width = 30
height = 30

MAX_THROTTLE = 3
MAX_DELTA_THETA = 4

# create robot image
org_robot_img = pygame.image.load("robot.png")
org_robot_img = pygame.transform.scale(org_robot_img, [width, height])

# create a robot surface to be added to the main window
robot = pygame.Surface([width, height], pygame.SRCALPHA)
# add the robot image to the robot
# robot robot left to face "forward"
robot.blit(org_robot_img, [0, 0])

def draw():
    """Draw robot to screen"""

    # Add the robot surface to the main window surface.
    # The x and y from the field module is given from the center
    rotated_robot = pygame.transform.rotate(robot, theta)
    win.screen.blit(rotated_robot, rotated_robot.get_rect(center=(x, y)))


def drive():

    # use global x and y
    global x, y, delta_theta, theta

    # reset theta
    delta_theta = 0

    # throttle
    throttle = 0

    # update keyboard arrows
    ds.check_keyboard()

    # print of anything is pressed
    if ds.UP_PRESSED:
        # increase throttle when pressing forward
        throttle += MAX_THROTTLE
    if ds.DOWN_PRESSED:
        # decrease throttle when pressing forward
        throttle -= MAX_THROTTLE
    if ds.LEFT_PRESSED:
        # increase amount to turn by -2
        delta_theta += MAX_DELTA_THETA
    if ds.RIGHT_PRESSED:
        # increase amount to turn by 2
        delta_theta -= MAX_DELTA_THETA

    # turn robot
    turn(delta_theta)

    # calc new x and Y
    if not valid_drive(throttle):
        throttle = 0
    x += throttle * math.cos(theta * math.pi/180)
    y -= throttle * math.sin(theta * math.pi/180)
    # print("x, y = (" + str(x) +", " + str(y) + ")")


def turn(angle):
    global theta
    # print("angle: " + str(angle))
    # print("theta " + str(theta))

    # increase field angle
    theta += angle


def valid_drive(throttle):
    temp_x = throttle * math.cos(theta * math.pi/180)
    temp_y = throttle * math.sin(theta * math.pi/180)

    new_x = x + (temp_x * 2)
    new_y = y - (temp_y * 2)
    # get original robot rect
    robot_rect = robot.get_rect(center=(new_x, new_y))

    # create a rect for where the robot WILL be so it can avoid
    # running into something before it runs into it
    print(robot_rect)

    # check if robot has run into any rockets first...
    for rocket in field.rockets:
        if robot_rect.colliderect(rocket):
            return False

    # if robot is going left and at left edge
    if x <= field.X_PADDING and temp_x < 0:
        return False
    # if robot is going right and at right edge
    elif x >= win.WIDTH - field.X_PADDING and temp_x > 0:
        return False
    # if robot is going up and at top edge
    elif y <= field.Y_PADDING and temp_y > 0:
        return False
    # if robot is going down and is on bottom edge
    elif y >= win.HEIGTH - field.Y_PADDING and temp_y < 0:
        return False
    # if robot is GOING to collide with the cargo ship
    elif robot_rect.colliderect(field.cargo_ship):
        return False
    else:
        return True


def stop():
    ds.robot_stop = True


def forward(amount):
    """Drive the robot forward a given amount"""

    # grab global vars
    global x, y

    throttle = 2

    # scale the amount to be a reasonable number of pixels
    amount *= 2

    # loop through the pixels to move
    for step in range(1, amount, throttle):
        # calc new x and Y
        if not valid_drive(throttle):
            throttle = 0
        x += throttle * math.cos(theta * math.pi / 180)
        y -= throttle * math.sin(theta * math.pi / 180)

        win.draw_bg()
        draw()
        win.flip()


def backwards(amount):
    """Drive the robot forward a given amount"""

    # grab global vars
    global x, y

    throttle = 2

    # scale the amount to be a reasonable number of pixels
    amount *= 2

    # loop through the pixels to move
    for step in range(1, amount, throttle):
        # calc new x and Y
        if not valid_drive(throttle):
            throttle = 0
        x -= throttle * math.cos(theta * math.pi / 180)
        y += throttle * math.sin(theta * math.pi / 180)

        win.draw_bg()
        draw()
        win.flip()


def turn_right(degrees):
    global theta

    delta_theta = 2

    for step in range(1, degrees, delta_theta):
        theta -= delta_theta
        win.draw_bg()
        draw()
        win.flip()


def turn_left(degrees):
    global theta

    delta_theta = 2

    for step in range(1, degrees, delta_theta):
        theta += delta_theta
        win.draw_bg()
        draw()
        win.flip()