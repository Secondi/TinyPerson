__author__ = 'SecondiNation'

from .base import ScreenComponent
from drawille import line

class Line(ScreenComponent):
    def __init__(self, x1, y1, x2, y2, screen_x, screen_y, is_test=False):
        state = {
            'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2
        }

        super(Line, self).__init__(state, screen_x, screen_y, is_test)

    def draw(self, terminal_x, terminal_y):
        """
        Translate line to
        """
        state = self.get_state()

        x, y = self.translate_xy(state['x1'], state['y1'], terminal_x, terminal_y)
        x2, y2 = self.translate_xy(state['x2'], state['y2'], terminal_x, terminal_y)

        return line(x, y, x2, y2)