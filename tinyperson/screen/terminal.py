__author__ = 'SecondiNation'

from Queue import Empty
import curses
from threading import Thread

from drawille import Canvas, line

from ..base import BaseComponent


class TerminalScreen(BaseComponent):
    """
    Hello, this is the screen controller for my game.

    This is a handler for getting drawille onto the curses interface.

    On each draw attempt, this will take the assets from the game world and attempt to draw them on screen.

    terminal_window provides units in y,x format. This game provides units in x,y
    """

    BLANK_TERMINAL = {
        'frames': 0,
        'elapsed_time': 0
    }

    def __init__(self, terminal_window, initial_state, is_test):
        """
        Assume that curses has already been initialize
        :param initial_state: first state of the terminal
        :param is_test: is this being tested/debugged?
        :return: n/a
        """
        super(TerminalScreen, self).__init__(initial_state, is_test)
        self.terminal_window = terminal_window
        self.canvas = Canvas()
        self.width, self.height = self._terminal_size()

        if is_test:
            print "terminal is %s wide, %s high" % (self.width, self.height)

        terminal_thread = Thread(
            group=None,
            target=curses.wrapper,
            name="Screen Thread",
            args=(self.draw,),
            kwargs={}
        )

        terminal_thread.start()


    def _is_frame_valid(self, frame):
        return frame is not None and len(frame) > 0

    def _terminal_size(self):
        """
        :return: (width, height) of the terminal window
        """
        height, width = self.terminal_window.getmaxyx()
        return width, height

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
            self.width, self.height = self._terminal_size()

            try:
                frame = self.queue_in.get(timeout=2)
            except Empty:
                if self.is_test:
                    print "there aren't any frames to render, lets cycle through for kicks"

            if self._is_frame_valid(frame):
                self.canvas.set(0, 0)
                self.canvas.set(self.width, self.height)

                for asset in frame:
                    for xp, yp in asset.draw(self.width, self.height):
                        if self.is_test:
                            print "terminal is %s wide, %s high" % (self.width, self.height)
                            print "point x: %s, point y: %s" % (xp, yp)

                        if xp >= 0 and xp <= self.width and yp >= 0 and yp <= self.height:
                            self.canvas.set(xp, yp)

                for x,y in line(0,0,158, 45):
                    self.canvas.set(x,y)

                rendered_frame = self.canvas.frame() + '\n'
                terminal_screen.addstr(0, 0, rendered_frame)
                terminal_screen.refresh()
                self.canvas.clear()

                frame = None