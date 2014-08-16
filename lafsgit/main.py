import sys

from twisted.internet import reactor, stdio

from mock import sentinel

from lafsgit import gitcontroller, protocol


def main(args = sys.argv[1:]):
    [remote, url] = args

    lafsclient = sentinel.lafsclient # Stub.
    ctl = gitcontroller.GitController(lafsclient)
    ldp = protocol.LineDispatcherProtocol(ctl.handle_git_command)

    stdio.StandardIO(ldp)

    reactor.run()
