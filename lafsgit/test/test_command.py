from twisted.trial.unittest import TestCase

from mock import Mock

from lafsgit.command import CommandProtocol


class CommandProtocolTests (TestCase):

    def setUp(self):
        self.mockreactor = Mock()
        self.fakeurl = 'URI:FAKE_CAP'
        self.fakenameish = 'trace::' + self.fakeurl
        self.proto = CommandProtocol(self.mockreactor, self.fakenameish, self.fakeurl)


    def test_capabilities(self):
        self.proto.connectionMade()
