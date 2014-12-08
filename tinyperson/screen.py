__author__ = 'SecondiNation'

from Queue import Empty

from .base import BaseComponent


class ScreenComponent(BaseComponent):
    pass


class TerminalScreen(BaseComponent):
    """
    Hello, this is the screen controller for my game.

    This is a handler for the curses interface.

    On each draw attempt, this will take the assets from the game world and attempt to draw them on screen
    """
    BLANK_TERMINAL = {
        'frames': 0,
        'elapsed_time': 0
    }

    def __init__(self, initial_state, test):
        super(TerminalScreen, self).__init__(initial_state, test)

    def is_frame_valid(self, frame):
        if self.is_test:
            print "check if frame valid"

        return len(frame) > 0

    def draw(self, test=False):
        """
        Push

        From self.queue_in, check for a tuple of items to be rendered on the terminal.
        frame instances must inherit from ScreenComponent
        :return: Nothing
        """

        frame = None

        while self.active:
            try:
                frame = self.queue_in.get(timeout=2)
            except Empty:
                if test:
                    print "there aren't any frames to render, lets cycle through for kicks"

            if self.is_frame_valid(frame):
                if test:
                    print "frame is valid"
                print "lets print the frame"

                frame = None

