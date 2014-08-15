from twisted.protocols import basic

from lafsgit.logmixin import LogMixin


class LineDispatcherProtocol (basic.LineOnlyReceiver, LogMixin):
    """This delegates lines to a handler function which returns deferred outgoing lines.

    It is an abstraction that's only suitable for request/response
    line-based protocols, such as in git-remote-helpers.
    """

    def __init__(self, handler):
        LogMixin.__init__(self)
