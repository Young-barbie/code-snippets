# Module: retry_handler.py | Created: 2026-11-16 23:32:19

def run_with_retries(func, max_attempts: int = 3):
    last_error = None
    for _ in range(max_attempts):
        try:
            return func()
        except Exception as exc:
            last_error = exc
    raise RuntimeError(f'Task failed after {max_attempts} attempts') from last_error
