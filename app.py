# Update 18 - 2026-11-16 22:43:40
def batch_items(seq, size=10):
    return [seq[i:i + size] for i in range(0, len(seq), size)]
