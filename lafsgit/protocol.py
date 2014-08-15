from twisted.protocols import basic


class LineDispatcherProtocol (basic.LineOnlyReceiver):
    """This delegates lines to a handler function which returns deferred outgoing lines.

    It is an abstraction that's only suitable for request/response
    line-based protocols, such as in git-remote-helpers.
    """
