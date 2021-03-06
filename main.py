import robot_code
import field
import driver_station as ds
import window as win
import robot


def run():
    """main robot loop"""
    while True:
        # check if window has exited
        win.check_close()

        # check button presses
        win.check_buttons()

        # check keyboard events
        ds.check_keyboard()

        # redraw bg before anything else
        win.draw_bg()

        # draw the start button
        win.start_button.draw()

        if not ds.robot_stop:
            # loop though robot code
            robot_code.robot_code()

        # draw robot to screen
        robot.draw()

        # flip pygame window
        win.flip()



run()
