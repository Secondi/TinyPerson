__author__ = 'SecondiNation'

from Queue import Empty
from curses import KEY_RIGHT, KEY_LEFT
from threading import Thread

from .base import BaseComponent


class GameController(BaseComponent):
    """
    Parse items that are put onto the global @keys queue

    Wrap around the game controller state and return the keys that are currently being pressed
    """

    LEFT = KEY_LEFT
    RIGHT = KEY_RIGHT
    SPACE = 32  # binary:010 0000, Oct:040, Dec:32, Hex:20

    CONTROLS = (
        LEFT,  # Left Arrow
        RIGHT,  # Right Arrow
        SPACE,  # Jump
    )

    RESET_CONTROLLER = {
        LEFT: False,
        RIGHT: False,
        SPACE: False
    }

    def __init__(self, initial_state, is_test=False):
        super(GameController, self).__init__(initial_state, is_test)
        controller_thread = Thread(
            group=None,
            target=self._controller_loop,
            name="Controller Thread",
            args=(),
            kwargs={}
        )

        controller_thread.start()

    def _controller_loop(self):
        key_press = None

        # Check if Controller component is active
        while self.active:
            try:
                key_press = self.queue_in.get(timeout=2)
            except Empty:
                if self.is_test:
                    print "key didn't come, lets cycle through for kicks"

            if key_press in self.CONTROLS:
                # enable keypress in component state
                self.state[key_press] = True
                # reset key_press
                key_press = None

    def get_state(self):
        """
        Obtain the state of the game controller.
        reinitialize the component state
        :return: A dict of the relevant controls
        """
        temp = self.state

        # Reset the controller state
        self.state = self.initial_state.copy()

        return temp
