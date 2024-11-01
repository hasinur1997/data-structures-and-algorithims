class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []
        self.data = {}

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1

        self.cache.remove(key)
        self.cache.insert(0, key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if len(self.data) >= self.capacity:

            if key not in self.data:
                old_item = self.cache.pop()
                del self.data[old_item]

                self.cache.insert(0, key)
                self.data[key] = value

            else:
                self.cache.remove(key)
                self.cache.insert(0, key)
                self.data[key] = value
        else:
            self.cache.insert(0, key)
            self.data[key] = value


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)

print(lru.cache)

print(lru.get(1))

print(lru.cache)

lru.put(3, 3)
print(lru.cache)

print(lru.get(2))

lru.put(4, 4)

print(lru.cache)
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))