from twisted.trial.unittest import TestCase

from mock import ANY, call, patch

from lafsgit.main import main


class main_Tests (TestCase):

    @patch('twisted.internet.reactor.run')
    @patch('twisted.internet.stdio.StandardIO')
    @patch('lafsgit.gitcontroller.GitController')
    @patch('lafsgit.protocol.LineDispatcherProtocol')
    def test_double_colon_anonymous_url(self, m_LineDispatcherProtocol, m_GitController, m_StandardIO, m_run):
        # TODO: Specify lafsclient construction and plumbing.

        url = 'lafs::foo'

        main([url, url])

        self.assertEqual(
            m_GitController.mock_calls,
            [call(ANY)])

        self.assertEqual(
            m_LineDispatcherProtocol.mock_calls,
            [call(m_GitController.return_value.handle_git_command)])

        self.assertEqual(
            m_StandardIO.mock_calls,
            [call(m_LineDispatcherProtocol.return_value)])

        self.assertEqual(
            m_run.mock_calls,
            [call()])
