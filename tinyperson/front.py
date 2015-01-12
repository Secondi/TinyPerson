__author__ = 'SecondiNation'

import curses
from time import sleep
from threading import Thread

from .screen import TerminalScreen
from .controller import GameController
from screen import Line, Square


FPS = 60.0
PHYSICS = 30.0


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
        self.assets = []

    def draw_assets(self):
        while self.active:
            self.term.queue_in.put(self.assets)

            sleep(1. / FPS)

    def step_physics(self):
        test_line = Line(0, 0, 0, self.world_height, self.world_width, self.world_height)
        test_line2 = Line(self.world_width, 0, self.world_width, self.world_height, self.world_width, self.world_height)
        test_square = Square(self.world_width / 2, self.world_height / 2, 50, self.world_width, self.world_height)

        while self.active:
            new_state = test_line.get_state()
            new_state['x1'] += 0.6
            new_state['x2'] += 1
            test_line.set_state(new_state)

            ns = test_line2.get_state()
            ns['x1'] -= 1.2
            ns['x2'] -= 0.5
            test_line2.set_state(ns)

            self.assets = [test_line, test_line2, test_square]

            # should the game end?
            if not self.controller.is_enabled() or new_state['x1'] > self.world_width:
                self.goodbye()

            # wait for next step
            sleep(1. / PHYSICS)

    def start(self):
        render_thread = Thread(
            group=None,
            target=self.draw_assets,
            name="Render Loop",
            args=(),
            kwargs={}
        )

        physics_thread = Thread(
            group=None,
            target=self.step_physics,
            name="Physics Loop",
            args=(),
            kwargs={}
        )

        render_thread.start()
        physics_thread.start()


    def goodbye(self):
        self.active = False
        self.term.disable_component()
        self.controller.disable_component()

    def __exit__(self, type, value, traceback):
        if self.is_test:
            print type, value, traceback

        self.goodbye()

