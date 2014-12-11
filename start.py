__author__ = 'SecondiNation'

import locale

from tinyperson import GameLoop


# WORLD_RATIO 16:9
WORLD_WIDTH = 1920
WORLD_HEIGHT = 1080

locale.setlocale(locale.LC_ALL, "")

hello_game = GameLoop(WORLD_WIDTH, WORLD_HEIGHT)
hello_game.start()
