# Module: metrics.py | Created: 2026-11-17 17:54:23

def calculate_mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0

def calculate_range(values: list[float]) -> float:
    return (max(values) - min(values)) if values else 0.0
