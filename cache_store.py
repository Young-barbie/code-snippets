# Module: cache_store.py | Created: 2026-11-17 17:56:00

class MemoryCache:
    def __init__(self): self._store = {}
    def set(self, k, v): self._store[k] = v
    def get(self, k, d=None): return self._store.get(k, d)
