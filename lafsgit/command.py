import os
from twisted.internet import defer, reactor
from twisted.protocols import basic

from .logmixin import LogMixin


class CommandProtocol (basic.LineReceiver, LogMixin):

    GitCapabilities = ['option']

    delimiter = os.linesep

    def __init__(self, nameish, url):
        LogMixin.__init__(self)
        self.log.debug('%r', {'nameish': nameish, 'url': url})

    def connectionMade(self):
        self.log.debug('Ready for commands.')

    #def dataReceived(self, data): # Just for temporary tracing debug.
    #    self.log.debug('dataReceived(%r)', data)
    #    return basic.LineReceiver.dataReceived(self, data)

    def lineReceived(self, line):
        self.log.debug('Received line %r', line)

        if line == '':
            self._git_quit()
        else:
            args = line.split(' ', 1)
            name = args.pop(0)

            cmdfunc = getattr(self, 'git_' + name)

            d = defer.maybeDeferred(cmdfunc, *args)

            @d.addCallback
            def handle_response(response):
                self.log.debug('Sending response for %r:\n%s', name, response)
                self.transport.write(response + self.delimiter)

    def _git_quit(self):
        self.log.debug('Quit from git.')
        reactor.stop()

    def git_capabilities(self):
        return self.delimiter.join(self.GitCapabilities) + self.delimiter

    def git_list(self):
        return ('0' * 39) + '7 refs/heads/master' + self.delimiter # BUG: Implement me.
