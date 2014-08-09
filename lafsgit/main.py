import sys
import logging

from twisted.python import log as twistedlog
from twisted.internet import reactor, stdio

from lafsgit import command

DESCRIPTION = """
Support for a Tahoe-LAFS specific git remote.
"""


def main(args = sys.argv[1:]):
    init_logging()

    [nameish, url] = args

    stdio.StandardIO(command.CommandProtocol(nameish, url))
    reactor.run()


def init_logging():
    #gitdir = os.environ['GIT_DIR']
    #logpath = os.path.join(gitdir, 'lafs.log')
    logging.basicConfig(
        #filename=logpath,
        #filemode='a',
        stream=sys.stderr,
        format='%(asctime)s %(levelname) 5s %(name)s | %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S%z',
        level=logging.DEBUG)

    twistedlog.PythonLoggingObserver().start()
