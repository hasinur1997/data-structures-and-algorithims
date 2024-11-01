class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        node = Node(key, value)

        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node

    def remove(self, item):
        if self.head is None:
            return
        if self.head.key == item:
            self.head = self.head.next

        current = self.head
        prev = None

        while current:
            if current.key == item:
                prev.next = current.next
                break
            prev = current
            current = current.next


    def print(self):
        if self.head is None:
            return

        current = self.head

        while current:
            print(current.val)

            current = current.next


class MyHashMap:

    def __init__(self):
        self.size = 100
        self.data = [None] * self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)

        if self.data[index] is None:
            self.data[index] = LinkedList()
            self.data[index].insert(key, value)

        else:
            li = self.data[index]
            current = li.head

            while current:
                if current.key == key:
                    current.val = value
                    break
                current = current.next

            else:
                li.insert(key, value)


    def get(self, key: int) -> int:
        index = self._hash(key)

        if self.data[key] is None:
            return -1

        li = self.data[index]
        current = li.head

        while current:
            if current.key == key:
                return current.val

            current = current.next

        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)

        if self.data[index] is not None:
            li = self.data[index]
            li.remove(key)

    def _hash(self, key):
        return hash(key) % self.size



hash_map = MyHashMap()

hash_map.put(1, 1)
hash_map.put(2, 2)

print(hash_map.get(1))
print(hash_map.get(3))

hash_map.put(2, 1)

print(hash_map.get(2))

hash_map.remove(2)

print(hash_map.get(2))
