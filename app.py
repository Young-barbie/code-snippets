# Update 2 - 2026-11-16 23:15:00
import datetime

def log_status(msg):
    timestamp = datetime.datetime.now().isoformat()
    print(f'[{timestamp}] {msg}')
