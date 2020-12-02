class MLRegistry:
    def __init__(self):
        self.endpoints = {}

    def add_algorithm(self, endpoint_name, algorithm_object):
        self.endpoints[endpoint_name] = algorithm_object