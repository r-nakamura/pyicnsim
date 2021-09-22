#!/usr/bin/env python3

from collections import defaultdict

class Metrics:
    def __init__(self):
        self.nhit = defaultdict(int)
        self.nreceived = defaultdict(int)
        self.nhop = defaultdict(list)

    def cache_hit_ratio_for_content(self, c):
        """Calculate cache hit ratio for content C, which is defined as the
        ratio of the number of cache hits to the number of received
        request packets."""
        if c in self.nhit and c in self.nreceived:
            return self.nhit[c] / self.nreceived[c]
        else:
            return None
