# Module: batch_processor.py | Created: 2026-11-17 17:55:25

def chunk_sequence(items: list, chunk_size: int = 10) -> list[list]:
    if chunk_size <= 0: raise ValueError('chunk_size must be positive')
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
