__author__ = 'SecondiNation'

from ..base import BaseComponent


class ScreenComponent(BaseComponent):
    def __init__(self, initial_state, world_width, world_height, is_test=False):
        super(ScreenComponent, self).__init__(initial_state, is_test)
        self.world_width = world_width
        self.world_height = world_height

    def translate_xy(self, x, y, terminal_width, terminal_height):
        """
        Example: y is 100 in world coordinate
        -> terminal_width = 158
        -> terminal_height = 45
        -> world_height = 108

        y/world_height = trans_y/terminal_height
        translated_y -> terminal_height * (y/world_height)
        translated_y -> 45 * (100/108)

        :param x: x position in world
        :param y: y position in world
        :param terminal_x: width of terminal
        :param terminal_y: height of terminal
        :return: x,y of world translated to position on screen
        """
        return terminal_width * (x / self.world_width), terminal_height * (y / self.world_height)
