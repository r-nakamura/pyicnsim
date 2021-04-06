#!/usr/bin/env python3

from collections import OrderedDict
import random

class Requester:
    def __init__(self, request_rate=0.1, delta=1):
        self.request_rate = request_rate
        self.request_ratio = OrderedDict() # CDF
        self.delta = delta

    def generate_request(self):
        "Generate content request following a given request rate."
        if random.uniform(0, 1) < self.request_rate * self.delta:
            return self.select_content()
        else:
            return None

    def select_content(self):
        "Randomly Select content to be requested."
        rand = random.uniform(0, 1)
        for c, prob in self.request_ratio.items():
          if rand <= prob:
              return c

    def preprocess_request_ratio(self, request_ratio):
        "Prepare CDF of request ratio."
        prob = 0
        for c in sorted(request_ratio.keys()):
            prob += request_ratio[c]
            self.request_ratio[c] = prob
