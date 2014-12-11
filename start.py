__author__ = 'SecondiNation'

from tinyperson import GameLoop

# WORLD_RATIO 16:9
WORLD_WIDTH = 1920
WORLD_HEIGHT = 1080

hello_game = GameLoop(WORLD_WIDTH, WORLD_HEIGHT)
hello_game.start()
