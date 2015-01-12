__author__ = 'SecondiNation'

import curses
from time import sleep
from threading import Thread

from .screen import TerminalScreen
from .controller import GameController
from .screen import Line, Square
from .physics import PhysicsWorld


FPS = 60.0
RENDER_STEP = 1. / FPS
PHYSICS_FPS = 30.0
PHYSICS_STEP = 1. / PHYSICS_FPS


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

        self.physics = PhysicsWorld()

    def draw_assets(self):
        while self.active:
            self.term.queue_in.put(self.assets)

            sleep(RENDER_STEP)

    def step_physics(self):
        while self.active:
            self.physics.step(PHYSICS_STEP)

            # should the game end?
            if not self.controller.is_enabled():
                self.goodbye()

            sleep(PHYSICS_STEP)

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

