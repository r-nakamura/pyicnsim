#!/usr/bin/env python3

class Scheduler():
    def __init__(self, time=0, delta=1, max_time=100000):
        self.time = time   # simulation clock [ms]
        self.delta = delta # slot length [ms]
        self.max_time = max_time
        self.nodes = []
        self.origin = {}

    def advance(self):
        """Advance time of simulation."""
        self.time += self.delta

    def is_running(self):
        """Check if simulation is still running."""
        return self.time <= self.max_time
