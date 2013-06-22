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
        self.proto.dataReceived('capabilities\n')

        expected = '\n'.join(CommandProtocol.GitCapabilities) + '\n\n'

        self.assertEqual(expected, self.trans.value())
