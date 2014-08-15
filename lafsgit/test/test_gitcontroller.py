from twisted.trial.unittest import TestCase

from mock import MagicMock, call, patch

from lafsgit.gitcontroller import GitController


class GitControllerTests (TestCase):

    def setUp(self):
        self.m_lafsclient = MagicMock()

        with patch('logging.getLogger') as m_getLogger:
            self.m_getLogger = m_getLogger
            self.gc = GitController(self.m_lafsclient)


    def test__init__calls_getLogger(self):
        # Note: This asserts there are no log calls in the constructor:
        self.assertEqual(self.m_getLogger.mock_calls, [call('GitController')])


    def test_handle_git_command_capabilities(self):
        self.assertEqual(['push'], self._hgcs('capabilities'))


    def _hgcs(self, *commandlines):
        """handle_git_command(s)

        This asserts that all but the last command returns None.
        It returns the result of the last command.
        """
        lastresult = None
        for cmd in commandlines:
            result = self.gc.handle_git_command(cmd)
            self.assertIsNone(lastresult)
            lastresult = result
        return lastresult
