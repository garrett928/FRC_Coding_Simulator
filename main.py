import robot_code
import field
import driver_station as ds
import window as win


def run():
    """main robot loop"""
    while True:
        # check if window has exited
        win.check_close()

        # check keyboard events
        ds.check_keyboard()

        # redraw bg before anything else
        win.draw_bg()

        # loop though robot code
        robot_code.robot_code()

        # flip pygame window
        win.flip()


run()
