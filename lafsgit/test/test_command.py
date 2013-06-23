from twisted.trial.unittest import TestCase
from twisted.test import proto_helpers

from lafsgit.command import CommandProtocol


class CommandProtocolTests (TestCase):

    def setUp(self):
        self.fakeurl = 'URI:FAKE_CAP'
        self.fakenameish = 'trace::' + self.fakeurl
        self.proto = CommandProtocol(self.fakenameish, self.fakeurl)
        self.trans = proto_helpers.StringTransport()
        self.proto.makeConnection(self.trans)


    def test_capabilities(self):
        caps = CommandProtocol.GitCapabilities

        self._check_cmd_io(
            input = 'capabilities\n',
            expected = '\n'.join(caps) + '\n\n')


    def test_valid_option_accepted(self):
        self._check_cmd_io('option progress true\n', 'ok\n')
        self._check_cmd_io('option progress false\n', 'ok\n')
        self._check_cmd_io('option verbosity 0\n', 'ok\n')
        self._check_cmd_io('option progress true\n', 'ok\n')
        self._check_cmd_io('option verbosity 3\n', 'ok\n')


    def _check_cmd_io(self, input, expected):
        self.trans.clear()
        self.proto.dataReceived(input)
        self.assertEqual(expected, self.trans.value())
