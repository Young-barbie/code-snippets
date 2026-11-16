# Module: retry_handler.py | Created: 2026-11-16 23:37:08

def run_with_retries(func, max_attempts: int = 3):
    for _ in range(max_attempts):
        try: return func()
        except Exception: pass
    raise RuntimeError('Max retries exceeded')
