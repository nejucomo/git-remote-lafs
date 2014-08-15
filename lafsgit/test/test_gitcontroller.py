from twisted.trial.unittest import TestCase

from mock import call, patch, sentinel

from lafsgit.gitcontroller import GitController


class GitControllerTests (TestCase):

    @patch('logging.getLogger')
    def test__init__calls_getLogger(self, m_getLogger):

        GitController(sentinel.lafsclient)

        # Note: This asserts there are no log calls in the constructor:
        self.assertEqual(m_getLogger.mock_calls, [call('GitController')])
