import sys
import logging

from twisted.trial.unittest import TestCase

import mock

from lafsgit import logmixin



class main_Tests (TestCase):

    @mock.patch('logging.getLogger')
    def test_LogMixin__init__(self, m_getLogger):

        logmixin.LogMixin()

        m_getLogger.assert_called_with('LogMixin')
