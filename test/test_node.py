#!/usr/bin/env python3

from icnsim.node import Node
from icnsim.runner import Runner

class TestNode():
    def test__find_caching_node(self):
        runner = Runner()
        v1 = Node(runner, id_=1)
        v2 = Node(runner, id_=2)
        v3 = Node(runner, id_=3)
        runner.nodes[1] = v1
        runner.nodes[2] = v2
        runner.nodes[3] = v3

        v2.store("dummy1")
        assert v1._find_caching_node([1, 2, 3], "dummy1") == (1, 2)
        assert v2._find_caching_node([2, 3], "dummy1") == (0, 2)
        assert v1._find_caching_node([1, 2, 3], "dummy2") == (2, 3)

    def test__update_cache(self):
        runner = Runner()
        v1 = Node(runner, id_=1)
        v2 = Node(runner, id_=2)
        v3 = Node(runner, id_=3)
        runner.nodes[1] = v1
        runner.nodes[2] = v2
        runner.nodes[3] = v3

        v1.origin_tbl["dummy1"] = 3; v1.origin_tbl["dummy2"] = 3
        v2.origin_tbl["dummy1"] = 3; v2.origin_tbl["dummy2"] = 3
        v3.origin_tbl["dummy1"] = 3; v3.origin_tbl["dummy2"] = 3

        v1._update_cache(2, [1, 2, 3], "dummy1")
        assert v1.is_storing("dummy1") == True
        assert v2.is_storing("dummy1") == True
        assert v3.is_storing("dummy1") == False

        v1._update_cache(1, [1, 2, 3], "dummy2")
        assert v1.is_storing("dummy2") == True
        assert v2.is_storing("dummy2") == True
        assert v3.is_storing("dummy2") == False

    def test_store(self):
        runner = Runner()
        v = Node(runner)

        v.store("dummy1")
        assert v.is_storing("dummy1") == True
        assert v.is_storing("dummy2") == False

    def test_get_path(self):
        runner = Runner()
        v = Node(runner)

        v.origin_tbl[1] = 3
        v.path_tbl[3] = [1, 2, 3]

        assert v.get_path(1) == [1, 2, 3]
