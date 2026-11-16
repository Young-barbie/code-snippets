# Updated: 2026-11-16 23:24:25

def batch_items(seq: list, size: int = 10) -> list:
    return [seq[i:i + size] for i in range(0, len(seq), size)]
