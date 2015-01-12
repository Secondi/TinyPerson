__author__ = 'SecondiNation'
import logging

import pymunk


logger = logging.getLogger("TinyPerson.physics")


class PhysicsWorld(object):
    def __init__(self, gravity=-900.0):
        self.world = pymunk.Space()
        self.world.gravity = (0.0, gravity)
        self.active = True

        logger.debug("Initialized physics world")

    def add(self, asset):
        self.world.add(asset)

    def remote(self, asset):
        self.world.remove(asset)

    def destroy(self):
        self.active = False

    def step(self, dt):
        if self.active:
            self.world.step(dt)
        else:
            logger.warn("The physics loop is not active")