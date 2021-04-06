#!/usr/bin/env python3

class LRUCache:
    def __init__(self, cache_size=10):
        self.size = cache_size
        self.buf = []

    def cache(self, c):
        """Cache a given content C in LRU manner."""
        if self.lookup(c):
            return

        if self.is_full():
            self.evict()
        self.inject(c)

    def inject(self, c):
        """Inject newly-arrived content C to buffer."""
        if not c in self.buf:
            self.buf.append(c)

    def evict(self):
        """Evict least-recently used contents from buffer."""
        self.buf.pop(0)

    def lookup(self, c):
        """Check if content C exists in buffer and update buffer."""
        if c in self.buf:
            idx = self.buf.index(c)
            self.buf.pop(idx)
            self.buf.append(c)
            return True
        else:
            return False

    def is_full(self):
        """Check if the cache size if full."""
        if len(self.buf) == self.size:
            return True
        else:
            return False

