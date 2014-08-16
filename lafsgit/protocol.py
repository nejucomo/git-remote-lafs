from twisted.protocols import basic
from twisted.internet import defer

from lafsgit.logmixin import LogMixin


class LineDispatcherProtocol (basic.LineOnlyReceiver, LogMixin):
    """This delegates lines to a handler function which returns deferred outgoing lines.

    It is an abstraction that's only suitable for request/response
    line-based protocols, such as in git-remote-helpers.
    """

    delimiter = b'\n'

    def __init__(self, handler):
        LogMixin.__init__(self)
        self._handler = handler

    def lineReceived(self, line):
        self._log.debug('Received: %r', line)

        d = defer.maybeDeferred(self._handler, line)

        @d.addCallback
        def responses_received(lines):
            if lines is not None:
                for line in lines:
                    self._log.debug('Sending: %r', line)
                    self.transport.write(line + self.delimiter)
