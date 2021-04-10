#!/usr/bin/env python3

import icnsim.cs
import icnsim.metrics
import icnsim.requester

class Node:
    def __init__(self, id_=None, request_rate=0.1, cache_size=10):
        self.id_ = id_
        self.requester = icnsim.requester.Requester(request_rate=request_rate)
        self.cs = icnsim.cs.LRUCache(cache_size=cache_size)
        self.metrics = icnsim.metrics.Metrics()

        self.origin_tbl = {}
        self.path_tbl = {}

    def advance(self):
        """Run node's operation, i.e., requesting content and updating caches
           at routers."""
        c = self.requester.generate_request()
        if not c == None:
            self.request_content(c)

    def request_content(self, c):
        """Issue a request packet for content C."""
        path = self.get_path(c)
        caching_node = self._find_caching_node(path, c)
        self._update_cache(caching_node[0], path, c)

    def _find_caching_node(self, path, c):
        """Find node caching content C on PATH and return tupple (NODE,
        INDEX)."""
        for idx, v in enumerate(path):
            v.metrics.nreceived[c] += 1
            if v.is_storing(c):
                v.metrics.nhit[c] += 1
                return (idx, v)
        return (len(path) - 1, path[-1])

    def _update_cache(self, idx, path, c):
        """Update caches from SELF to IDX-th routers on PATH."""
        # caching strategy LCE (Leave Copy Everywhere)
        for v in path[:idx + 1]:
            if v.id_ != self.origin_tbl[c]: # origin router does not cache original content
                v.store(c)

    def store(self, c):
        """Cache content C to own Content Store."""
        self.cs.cache(c)

    def is_storing(self, c):
        """Check if content C is cached at own Content Store."""
        return self.cs.lookup(c)

    def get_path(self, c):
        """Return a path from SELF to origin node storing content C."""
        s = self.origin_tbl[c]
        return self.path_tbl[s]
