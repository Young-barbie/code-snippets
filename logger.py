# Module: logger.py | Created: 2026-11-17 17:54:47

import datetime

def log_event(level: str, message: str) -> str:
    entry = f'[{datetime.datetime.now().isoformat()}] [{level.upper()}] {message}'
    print(entry)
    return entry
