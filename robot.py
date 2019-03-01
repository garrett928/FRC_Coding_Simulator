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
width = 60
height = 60

# create robot image
org_robot_img = pygame.image.load("robot.png")

# create a robot surface to be added to the main window
robot = pygame.Surface([width, height], pygame.SRCALPHA)
# add the robot image to the robot
# robot robot left to face "forward"
robot.blit(pygame.transform.rotate(org_robot_img, -90), [0, 0])


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
        throttle += 4
    if ds.DOWN_PRESSED:
        # decrease throttle when pressing forward
        throttle -= 4
    if ds.LEFT_PRESSED:
        # increase amount to turn by -2
        delta_theta += 4
    if ds.RIGHT_PRESSED:
        # increase amount to turn by 2
        delta_theta -= 4

    # turn robot
    turn(delta_theta)

    # calc new x and Y
    x += throttle * math.cos(theta * math.pi/180)
    y -= throttle * math.sin(theta * math.pi/180)
    print("x, y = (" + str(x) +", " + str(y) + ")")


def turn(angle):
    global theta
    print("angle: " + str(angle))
    print("theta " + str(theta))

    # increase field angle
    theta += angle
