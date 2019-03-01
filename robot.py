import field
import pygame
import window as win
import driver_station as ds


# robot x and y cord, from center of robot not top left
x = field.RED_2[0]
y = field.RED_2[1]

# robot width and height
width = 60
height = 60

# create robot image
robot_img = pygame.image.load("robot.png")
# robot robot left to face "forward"
robot_img = pygame.transform.rotate(robot_img, -90)
# create a robot surface to be added to the main window
robot = pygame.Surface([width, height])
# add the robot image to the robot
robot.blit(robot_img, [0, 0])


def draw():
    """Draw robot to screen"""
    # Add the robot surface to the main window surface.
    # The x and y from the field module is given from the center
    win.screen.blit(robot, [x - width/2, y - height/2])


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
        y+= 1
