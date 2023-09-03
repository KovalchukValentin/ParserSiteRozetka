import math


class Analyst:
    def __init__(self):
        self.count_values = 0
        self.sum_values = 0
        self.min_value = math.inf
        self.max_value = 0

    def get_averange(self):
        return self.sum_values / self.count_values

    def _get_averange(self, values):
        pass

    def add_values(self, values: list):
        self.count_values += len(values)
        self.sum_values += sum(values)
        max_value = max(values)
        min_value = min(values)
        if self.max_value < max_value:
            self.max_value = max_value
        if self.min_value > min_value:
            self.min_value = min_value
