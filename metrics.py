# Module: metrics.py | Created: 2026-11-16 23:35:46

def calculate_mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0

def calculate_range(values: list[float]) -> float:
    return (max(values) - min(values)) if values else 0.0
