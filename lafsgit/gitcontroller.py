import sys

from twisted.internet import reactor

from lafsgit.logmixin import LogMixin


UnknownCommandExitStatus = 1


class GitController (LogMixin):
    def __init__(self, lafsclient):
        LogMixin.__init__(self)

    def handle_git_command(self, line):
        if line == 'capabilities':
            return ['push']
        else:
            reactor.stop()
            sys.stderr.write('Unknown Command %r\n' % (line,))
            sys.exit(UnknownCommandExitStatus)
