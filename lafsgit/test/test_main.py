import sys
import logging

from twisted.trial.unittest import TestCase

import mock

from lafsgit import main



class main_Tests (TestCase):

    @mock.patch('twisted.internet.reactor.run')
    @mock.patch('twisted.internet.stdio.StandardIO')
    @mock.patch('lafsgit.command.CommandProtocol')
    @mock.patch('twisted.python.log.PythonLoggingObserver')
    @mock.patch('logging.basicConfig')
    def test_main_named_origin(self, m_basicConfig, m_PythonLoggingObserver, m_CommandProtocol, m_StandardIO, m_run):

        origin = 'tahoe-origin'
        url = 'lafs://URI:DIR2-etc-etc'

        main.main([origin, url])

        m_basicConfig.assert_called_with(
            stream=sys.stderr,
            format=mock.ANY,
            datefmt=mock.ANY,
            level=logging.DEBUG)

        self.assertEqual(
            m_PythonLoggingObserver.mock_calls,
            [mock.call(),
             mock.call().start()])

        m_CommandProtocol.assert_called_with(origin, url)
        m_StandardIO.assert_called_with(m_CommandProtocol.return_value)
        m_run.assert_called_with()

