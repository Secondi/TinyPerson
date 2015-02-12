__author__ = 'Brendon Muschamp'
__copyright__  = "Copyright 2015, Marbon Bros Ltd"
__license__ = "GPLv3"
__status__ = "prototype"
__version__ = "0.1.0"
__email__ = "brendon@marbonbros.com"

import locale

from tinyperson import GameLoop


# WORLD_RATIO 16:9
WORLD_WIDTH = 80
WORLD_HEIGHT = 50

locale.setlocale(locale.LC_ALL, "")

hello_game = GameLoop(WORLD_WIDTH, WORLD_HEIGHT)
hello_game.start()
