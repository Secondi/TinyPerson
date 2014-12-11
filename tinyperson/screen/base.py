__author__ = 'SecondiNation'

from ..base import BaseComponent


class ScreenComponent(BaseComponent):
    def __init__(self, initial_state, screen_x, screen_y, is_test=False):
        super(ScreenComponent, self).__init__(initial_state, is_test)
        self.screen_x = screen_x
        self.screen_y = screen_y

    def translate_xy(self, x, y, terminal_x, terminal_y):
        return x * (terminal_x / self.screen_x), y * (terminal_y / self.screen_y)
