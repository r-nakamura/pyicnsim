#!/usr/bin/env python3

from icnsim.scheduler import Scheduler

class TestScheduler:
    def test_init(self):
        time, delta, max_time = 0, 1, 100000
        scheduler = Scheduler(time, delta, max_time)

        assert scheduler.time == time
        assert scheduler.delta == delta
        assert scheduler.max_time == max_time

    def test_advance(self):
        time, delta, max_time = 0, 1, 100000
        scheduler = Scheduler(time, delta, max_time)
        scheduler.advance()
        assert scheduler.time == time + delta

    def test_is_running(self):
        scheduler = Scheduler()

        scheduler.time, scheduler.max_time = 0, 100
        assert scheduler.is_running() == True

        scheduler.time, scheduler.max_time = 101, 100
        assert scheduler.is_running() == False
