# Module: validator.py | Created: 2026-11-16 23:36:32

def is_non_empty_string(value: object) -> bool:
    return isinstance(value, str) and len(value.strip()) > 0

def filter_valid_records(records: list) -> list:
    return [r for r in records if r is not None]
