__author__ = 'SecondiNation'

from Queue import Empty
import curses
from threading import Thread

from drawille import Canvas

from .base import BaseComponent


class ScreenComponent(BaseComponent):
    pass


class TerminalScreen(BaseComponent):
    """
    Hello, this is the screen controller for my game.

    This is a handler for using drawille on the curses interface.

    On each draw attempt, this will take the assets from the game world and attempt to draw them on screen
    """
    BLANK_TERMINAL = {
        'frames': 0,
        'elapsed_time': 0
    }

    def __init__(self, initial_state, is_test):
        """
        Assume that curses has already been initialize
        :param initial_state: first state of the terminal
        :param is_test: is this being tested/debugged?
        :return: n/a
        """
        super(TerminalScreen, self).__init__(initial_state, is_test)

        self.canvas = Canvas()
        self.width = 100
        self.height = 100
        terminal_thread = Thread(
            group=None,
            target=curses.wrapper,
            name="Screen Thread",
            args=(self.draw,),
            kwargs={}
        )

        terminal_thread.start()


    def is_frame_valid(self, frame):
        if self.is_test:
            print "check if frame is valid"

        return len(frame) > 0

    def draw(self, terminal_screen):
        """
        Push

        From self.queue_in, check for a tuple of items to be rendered on the terminal.
        frame instances must inherit from ScreenComponent
        :return: Nothing
        """

        frame = None
        terminal_screen.refresh()

        while self.active:
            try:
                frame = self.queue_in.get(timeout=2)
            except Empty:
                if self.is_test:
                    print "there aren't any frames to render, lets cycle through for kicks"

            if self.is_frame_valid(frame):
                if self.is_test:
                    print "frame is valid"
                    print "lets print the frame"

                self.canvas.set(0, 0)
                self.canvas.set(self.width, self.height)

                for asset in frame:
                    for x, y in asset.draw(self.height, self.width):
                        self.canvas.set(x, y)

                rendered_frame = self.canvas.frame() + '\n'
                terminal_screen.addstr(0, 0, rendered_frame)
                terminal_screen.refresh()
                self.canvas.clear()

                frame = None