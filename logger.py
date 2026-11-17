# Module: logger.py | Created: 2026-11-17 06:54:07

import datetime

def log_event(level: str, message: str) -> str:
    entry = f'[{datetime.datetime.now().isoformat()}] [{level.upper()}] {message}'
    print(entry)
    return entry
