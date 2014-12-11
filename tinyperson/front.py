__author__ = 'SecondiNation'

import curses
from time import sleep

from .screen import TerminalScreen
from .controller import GameController
from screen import Line


FPS = 25.0


class GameLoop(object):
    """
    Wrapper for the game
    """

    def __init__(self, world_width, world_height, is_test=False):
        if is_test:
            print "starting game"

        self.stdscr = curses.initscr()
        self.stdscr.refresh()
        self.world_width = world_width
        self.world_height = world_height

        self.term = TerminalScreen(self.stdscr, TerminalScreen.BLANK_TERMINAL, is_test)
        self.controller = GameController(self.stdscr, GameController.RESET_CONTROLLER, is_test)
        self.active = True

    def start(self):

        test_line = Line(40, 40, 100, 500, self.world_width, self.world_height)
        while self.active:
            new_state = test_line.get_state()
            new_state['x1'] += 10
            new_state['x2'] += 10
            test_line.set_state(new_state)

            self.term.queue_in.put([test_line])

            if new_state['x1'] > 1920:
               self.goodbye()

            sleep(1. / FPS)


    def goodbye(self):
        self.active = False
        self.term.disable_component()
        self.controller.disable_component()

    def __exit__(self, type, value, traceback):
        if self.is_test:
            print type, value, traceback

        self.goodbye()

