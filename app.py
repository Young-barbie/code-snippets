# Update 5 - 2026-11-16 23:17:02
def calculate_metrics(data):
    if not data:
        return 0
    return sum(data) / len(data)
