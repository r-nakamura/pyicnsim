#!/usr/bin/env python3

from icnsim.metrics import Metrics

class TestMetrics():
    def test_init(self):
        metrics = Metrics()
        assert metrics.nhit == {}
        assert metrics.nreceived == {}

    def test_cache_hit_ratio_for_content(self):
        metrics = Metrics()
        metrics.nhit["dummy1"] = 1
        metrics.nreceived["dummy1"] = 2
        assert metrics.cache_hit_ratio_for_content("dummy1") == 1 / 2
        assert metrics.cache_hit_ratio_for_content("dummy2") == None
