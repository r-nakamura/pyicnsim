#!/usr/bin/env python3

from icnsim.cs import LRUCache

class TestLRUCache:
    def test_init(self):
        cache_size = 10
        cs = LRUCache(cache_size=cache_size)

        assert cs.size == cache_size

    def test_cache(self):
        cs = LRUCache(cache_size=3)
        cs.cache(1)
        assert cs.buf == [1]
        cs.cache(2)
        assert cs.buf == [1, 2]
        cs.cache(1)
        assert cs.buf == [2, 1]
        cs.cache(3)
        assert cs.buf == [2, 1, 3]
        cs.cache(4)
        assert cs.buf == [1, 3, 4]

    def test_lookup(self):
        cs = LRUCache()

        cs.buf.append("dummy1")
        assert cs.lookup("dummy1") == True
        assert cs.lookup("dummy2") == False

    def test_is_full(self):
        cache_size = 1
        cs = LRUCache(cache_size=cache_size)

        assert cs.is_full() == False

        pkt = 1
        cs.buf.append(pkt)
        assert cs.is_full() == True
