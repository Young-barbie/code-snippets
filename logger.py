# Module: logger.py | Created: 2026-11-16 23:29:59

import datetime

def log_event(level: str, message: str) -> str:
    ts = datetime.datetime.now().isoformat()
    entry = f'[{ts}] [{level.upper()}] {message}'
    print(entry)
    return entry
