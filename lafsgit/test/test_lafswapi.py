from twisted.trial.unittest import TestCase
from twisted.test import proto_helpers

from lafsgit.lafswapi import LafsWapiClient


class LafsWapiTests (TestCase):

    def setUp(self):
        self.wapiurl = 'http://localhost:3456/'
        self.mreactor = proto_helpers.MemoryReactor()
        self.client = LafsWapiClient(self.mreactor, self.wapiurl)


    def test_create_mutable_directory(self):
        raise NotImplementedError()
