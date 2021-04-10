#!/usr/bin/env python3

from collections import defaultdict
import fileinput
import random

import graph_tools

import icnsim.node
import icnsim.scheduler

class Runner():
    def __init__(self, max_time=1000, delta=1, B=10, C=100, lambda_=0.1, alpha=0.8):
        self.B = B             # cache size at router
        self.C = C             # the number of contents
        self.lambda_ = lambda_ # request rate
        self.alpha = alpha

        self.scheduler = icnsim.scheduler.Scheduler(max_time=max_time, delta=delta)
        self.G = None # graph of routers

        self.nodes = {}
        self.origin_tbl = {}
        self.path_tbl = defaultdict(dict)

    def import_graph(self, fname, directed=False):
        """Import graph from a file with FNAME written in dot format."""
        self._import_dot(list(fileinput.input(fname)))

    def _import_dot(self, dot, directed=False):
        """Import graph from strings in dot format.  If DIRECTED is False,
           undirected graph is automatically converted to directed
           graph, which is mandatory for obtaining shortest-paths with
           graph-tools."""
        g = graph_tools.Graph(directed=directed)
        g.import_dot(dot)

        # convert to directed graph
        if directed == False:
            g._directed = True
            for u, v in g.unique_edges():
                if not g.has_edge(u, v):
                    g.add_edge(u, v)
                if not g.has_edge(v, u):
                    g.add_edge(v, u)

        self.G = g

    def add_nodes(self):
        """Prepare node objects based on graph G."""
        for v in self.G.vertices():
            node = icnsim.node.Node(
                id_=v, request_rate=self.lambda_, cache_size=self.B
            )
            self.nodes[v] = node

    def get_nodes(self):
        """Return node objects."""
        return self.nodes.values()

    def node_by_id(self, id_):
        """Return node object with ID_."""
        return self.nodes.get(id_, None)

    def preprocess(self):
        """Run simulation setup."""
        self._preprocess_content_origin()
        self._preprocess_path()
        self._preprocess_requester()

    def _preprocess_content_origin(self):
        """Randomly determine origin nodes."""
        V = self.G.vertices()
        for c in range(1, self.C + 1):
            origin = random.choice(V) # randomly choose origin router
            self.origin_tbl[c] = origin

        for k, v in self.nodes.items():
            v.origin_tbl = self.origin_tbl

    def _preprocess_path(self):
        """Obtain shortest-paths between any node pairs."""
        for s in self.G.vertices():
            for t in self.G.vertices():
                if s != t:
                    self.path_tbl[s][t] = self.G.shortest_paths(s, t)[0]
                else:
                    self.path_tbl[s][t] = [s]

                self.path_tbl[s][t] = [self.nodes[v] for v in self.path_tbl[s][t]]

        for id_, v in self.nodes.items():
            v.path_tbl = self.path_tbl[id_]

    def _preprocess_requester(self):
        """Configure request ratio following Zipf distribution with exponent
           parameter ALPHA."""
        request_ratio = {}
        for c in range(1, self.C + 1):
            request_ratio[c] = 1 / (c ** self.alpha)
        total = sum(request_ratio.values())

        for c in range(1, self.C + 1):
            request_ratio[c] /= total

        for v in self.get_nodes():
            v.requester.preprocess_request_ratio(request_ratio)

    def run(self):
        """Run simulation."""
        while self.scheduler.is_running():
            for v in self.get_nodes():
                v.advance()
            self.scheduler.advance()
