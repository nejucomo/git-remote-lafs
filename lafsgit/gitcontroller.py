from lafsgit.logmixin import LogMixin


class GitController (LogMixin):
    def __init__(self, lafsclient):
        LogMixin.__init__(self)
