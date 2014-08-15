from twisted.trial.unittest import TestCase

from mock import call, patch, sentinel

from lafsgit.protocol import LineDispatcherProtocol



class LineDispatcherProtocolTests (TestCase):

    @patch('logging.getLogger')
    def test__init__(self, m_getLogger):

        LineDispatcherProtocol(sentinel.handler)

        # Note: This asserts there are no log calls in the constructor:
        self.assertEqual(m_getLogger, [call('LineDispatcherProtocol')])
