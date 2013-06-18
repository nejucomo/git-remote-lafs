import logging


class LogMixin (object):
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
