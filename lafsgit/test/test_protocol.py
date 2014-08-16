from twisted.trial.unittest import TestCase

from mock import ANY, MagicMock, call, patch, sentinel

from lafsgit.protocol import LineDispatcherProtocol


class LineDispatcherProtocolTests (TestCase):

    @patch('logging.getLogger')
    def test__init__calls_getLogger(self, m_getLogger):

        LineDispatcherProtocol(sentinel.handler)

        # Note: This asserts there are no log calls in the constructor:
        self.assertEqual(m_getLogger.mock_calls, [call('LineDispatcherProtocol')])


    def _test_lineReceived(self, m_maybeDeferred):

        x = 'bananas!'

        ldp = LineDispatcherProtocol(sentinel.handler)
        ldp.transport = MagicMock()

        ldp.lineReceived(x)

        self.assertEqual(
            m_maybeDeferred.mock_calls,
            [call(sentinel.handler, x),
             call(sentinel.handler, x).addCallback(ANY)])

        # Retrieve the internal callback:
        (_, args, _) = m_maybeDeferred.mock_calls[1]
        (callback,) = args

        return callback, ldp.transport


    @patch('logging.getLogger')
    @patch('twisted.internet.defer.maybeDeferred')
    def test_lineReceived_None_response(self, m_maybeDeferred, m_getLogger):

        callback, m_transport = self._test_lineReceived(m_maybeDeferred)

        # Now test the callback with 0 response lines:
        callback(None)

        # Assert nothing was written:
        self.assertEqual(m_transport.mock_calls, [])


    @patch('logging.getLogger')
    @patch('twisted.internet.defer.maybeDeferred')
    def test_lineReceived_empty_response(self, m_maybeDeferred, m_getLogger):

        callback, m_transport = self._test_lineReceived(m_maybeDeferred)

        # Now test the callback with 0 response lines:
        callback([])

        # Assert nothing was written:
        self.assertEqual(m_transport.mock_calls, [])


    @patch('logging.getLogger')
    @patch('twisted.internet.defer.maybeDeferred')
    def test_lineReceived_with_response(self, m_maybeDeferred, m_getLogger):

        callback, m_transport = self._test_lineReceived(m_maybeDeferred)

        # Now test the callback with 0 response lines:
        callback(['a', 'b'])

        # Assert the responses are written:
        self.assertEqual(
            m_transport.mock_calls,
            [call.write('a\n'),
             call.write('b\n')])
