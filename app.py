# Updated: 2026-11-16 23:22:30

class DataProcessor:
    def __init__(self, items: list):
        self.items = items

    def filter_valid(self) -> list:
        return [item for item in self.items if item is not None]
