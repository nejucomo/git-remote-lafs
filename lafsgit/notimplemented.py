import os, sys


def not_implemented(tmpl, *args):
    sys.stderr.write('Not Implemented: %s\n' % (tmpl % args,))
    os._exit(-7)
