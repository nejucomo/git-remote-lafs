from lafsgit.logmixin import LogMixin


class GitController (LogMixin):
    def __init__(self, lafsclient):
        LogMixin.__init__(self)

    def handle_git_command(self, line):
        if line == 'capabilities':
            return ['push']
        else:
            raise NotImplementedError('Unsupported Command')
