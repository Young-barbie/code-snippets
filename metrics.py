# Module: metrics.py | Created: 2026-11-16 23:29:14

def calculate_mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)

def calculate_range(values: list[float]) -> float:
    return (max(values) - min(values)) if values else 0.0
