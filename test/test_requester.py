#!/usr/bin/env python3

from icnsim.requester import Requester

class TestRequester():
    def test_preprocess_request_ratio(self):
        request_ratio = {}
        request_ratio[1] = 0.1
        request_ratio[2] = 0.3
        request_ratio[3] = 0.6

        requester = Requester()
        requester.preprocess_request_ratio(request_ratio)
        assert requester.request_ratio[1] == 0.1
        assert requester.request_ratio[2] == 0.1 + 0.3
        assert requester.request_ratio[3] == 0.1 + 0.3 + 0.6
