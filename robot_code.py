import robot

"""
    Robot Rules:
        robot.drive: Uses the arrow keys to drive the robot
        robot.forwards: Moves the robot forwards a given amount
        robot.backwards: Moves the robot backwards a given amount
        robot.turn_left: Turns the robot left a given amount
        robot.turn_right: Turn the robot right a given amount
        robot.stop: Makes the robot program stop running
"""


def robot_code():
    robot.forward(20)
    robot.turn_right(90)
    robot.forward(40)
    robot.turn_left(90)
    robot.forward(40)
    robot.turn_right(90)
    robot.backwards(40)
    robot.stop()
