# Module: retry_handler.py | Created: 2026-11-17 17:55:43

def run_with_retries(func, max_attempts: int = 3):
    for _ in range(max_attempts):
        try: return func()
        except Exception: pass
    raise RuntimeError('Max retries exceeded')
