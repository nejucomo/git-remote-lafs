import os
from twisted.protocols import basic

from .logmixin import LogMixin


class CommandProtocol (basic.LineReceiver, LogMixin):

    delimiter = os.linesep

    def __init__(self, nameish, url):
        LogMixin.__init__(self)
        self.log.debug('%r', {'nameish': nameish, 'url': url})

    def connectionMade(self):
        self.log.debug('Ready for commands.')

    def lineReceived(self, line):
        self.log.debug('Received %r', line)

        from twisted.internet import reactor; reactor.stop(); raise NotImplementedError('lineReceived')
