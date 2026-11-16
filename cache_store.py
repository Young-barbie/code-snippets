# Module: cache_store.py | Created: 2026-11-16 23:37:27

class MemoryCache:
    def __init__(self): self._store = {}
    def set(self, k, v): self._store[k] = v
    def get(self, k, d=None): return self._store.get(k, d)
