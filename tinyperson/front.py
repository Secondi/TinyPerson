__author__ = 'SecondiNation'

import curses
from time import sleep

from .screen import TerminalScreen
from .controller import GameController
from screen import Line, Square

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

        test_line = Line(0, 0, 0, self.world_height, self.world_width, self.world_height)
        test_line2 = Line(self.world_width, 0, self.world_width, self.world_height, self.world_width, self.world_height)
        test_square = Square(self.world_width/2, self.world_height/2, 50, self.world_width, self.world_height)
        while self.active:
            new_state = test_line.get_state()
            new_state['x1'] += 1
            new_state['x2'] += 1
            test_line.set_state(new_state)

            ns = test_line2.get_state()
            ns['x1'] -= 1
            ns['x2'] -= 1
            test_line2.set_state(ns)

            self.term.queue_in.put([test_line, test_line2, test_square])

            sleep(1. / FPS)

            if not self.controller.is_enabled() or new_state['x1'] > self.world_width:
                self.goodbye()

    def goodbye(self):
        self.active = False
        self.term.disable_component()
        self.controller.disable_component()

    def __exit__(self, type, value, traceback):
        if self.is_test:
            print type, value, traceback

        self.goodbye()

