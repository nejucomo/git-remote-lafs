import os
import logging
from twisted.internet import defer, reactor
from twisted.protocols import basic

from .logmixin import LogMixin


class CommandProtocol (basic.LineReceiver, LogMixin):

    GitCapabilities = ['option', 'push']
    LogLevels = [logging.CRITICAL, logging.ERROR, logging.WARN, logging.INFO, logging.DEBUG]

    delimiter = '\n' # Based on a quick skim of transport-helper.c in git.


    def __init__(self, nameish, url):
        LogMixin.__init__(self)
        self._log.debug('%r', {'nameish': nameish, 'url': url})

        self._showProgress = False


    def connectionMade(self):
        self._log.debug('Ready for commands.')


    #def dataReceived(self, data): # Just for temporary tracing debug.
    #    self._log.debug('dataReceived(%r)', data)
    #    return basic.LineReceiver.dataReceived(self, data)


    def lineReceived(self, line):
        defer.maybeDeferred(self._raw_lineReceived, line)


    def _raw_lineReceived(self, line):
        self._log.debug('Received line %r', line)

        if line == '':
            self._git_quit()
        else:
            args = line.split(' ', 1)
            name = args.pop(0)

            cmdfunc = getattr(self, 'git_' + name)

            d = defer.maybeDeferred(cmdfunc, *args)

            @d.addCallback
            def handle_response(response):
                self._log.debug('Sending response for %r:\n%s', name, response)
                self.transport.write(response + self.delimiter)

            return d


    def _git_quit(self):
        self._log.debug('Quit from git.')
        reactor.stop()


    def git_capabilities(self):
        return self.delimiter.join(self.GitCapabilities) + self.delimiter


    def git_option(self, arg):
        try:
            self._raw_git_option(arg)
        except NotImplementedError:
            return 'unsupported'
        except Exception, e: # BUG: Dangerous!
            return 'error %r %r' % (e, '; '.join([ str(a) for a in e.args ]))
        else:
            return 'ok'


    def _raw_git_option(self, arg):
        name, optarg = arg.split(' ', 1)
        if name == 'progress':
            self._showProgress = {'true': True, 'false': False}[optarg]
        elif name == 'verbosity':
            gitlevel = int(optarg)
            loglevel = self.LogLevels[min(gitlevel, len(self.LogLevels) - 1)]
            # logging.getLogger().setLevel(loglevel) # FIXME: Temporarily disabled to force DEBUG level.
            self._log.debug('(disabled) Set log level to: git %r, python %r', gitlevel, logging.getLevelName(loglevel))
        else:
            raise NotImplementedError()


    def git_list(self, arg=None):
        return '' # BUG: Implement me.
