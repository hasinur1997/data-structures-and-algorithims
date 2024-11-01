class Node:
    def __init__(self, val=0):
        self.val = val
        self.use_count = 1

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counter = 0
        self.data = {}

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1

        self.data[key].use_count += 1

        return self.data[key].val

    def put(self, key: int, value: int) -> None:
        node = Node(value)

        if self.counter >= self.capacity:
            deletable_key = ''
            min = float('inf')
            for _key, _node in self.data.items():
                if _node.use_count < min:
                    min = _node.use_count
                    deletable_key = _key

            del self.data[deletable_key]
            self.data[key] = node

        else:
            self.data[key] = node
            self.counter += 1


obj = LFUCache(2)

obj.put(1, 1)
obj.put(2, 2)

print(obj.get(1))

obj.put(3, 3)



print(obj.get(2))
print(obj.get(3))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))