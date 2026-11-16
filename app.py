# Update 28 - 2026-11-16 22:50:59
def batch_items(seq, size=10):
    return [seq[i:i + size] for i in range(0, len(seq), size)]
