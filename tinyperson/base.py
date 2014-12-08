__author__ = 'SecondiNation'
from Queue import Queue


class BaseComponent(object):
    state = None
    queue_in = Queue()

    def __init__(self, initial_state, is_test=False):
        self.initial_state = initial_state.copy()
        self.state = initial_state.copy()
        self.active = True
        self.is_test = is_test

    def disable_component(self):
        """
        Toggle the active flag so any threads inside the component know it's time to turn off

        :return: The instance used to call this func
        """
        self.active = False

        return self

    def enable_component(self):
        """
        Toggle the active flag so that it's enabled...
        IMPORTANT: This doesn't start any threads required by the component

        :return: The instance used to call this func
        """
        self.active = True

        return self

    def get_state(self):
        """
        :return: The component state
        """

        return self.state