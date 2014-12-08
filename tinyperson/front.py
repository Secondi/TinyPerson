__author__ = 'SecondiNation'

import curses

from .screen import TerminalScreen
from .controller import GameController


class GameLoop(object):
    """
    Wrapper for the game
    """

    def __init__(self, is_test=False):
        if is_test:
            print "starting game"

        self.stdscr = curses.initscr()

        self.term = TerminalScreen(self.stdscr, TerminalScreen.BLANK_TERMINAL, is_test)
        self.controller = GameController(self.stdscr, GameController.RESET_CONTROLLER, is_test)

    def goodbye(self):
        self.term.disable_component()
        self.controller.disable_component()

    def __exit__(self, type, value, traceback):
        if self.is_test:
            print type, value, traceback

        self.goodbye()
