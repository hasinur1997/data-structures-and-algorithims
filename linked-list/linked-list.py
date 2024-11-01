from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, item):
        node = Node(item)
        self.count += 1

        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = node

    def prepend(self, item):
        node = Node(item)

        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def display(self):
        if self.is_empty():
            print("No thing display list is empty")
            return
        
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next

    def remove_first(self):
        if self.is_empty():
            raise Exception('Empty list')

        self.head = self.head.next
    
    def remove_last(self):
        if self.is_empty():
            raise Exception('Empty list')
        
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def remove_at(self, index):
        if index < 1:
            raise Exception('Invalid Index')

        if self.is_empty():
            raise Exception('Empty list')
        
        current = self.head
        target = index - 1
        k = 1
        prev = None

        # Get the target node
        while current.next and k <= target:
            prev = current
            current = current.next
            k += 1

        # Delete the node
        if index == 1:
            self.head = self.head.next
        elif k < target:
            print('index out of range')
        else:
            prev.next = current.next
        

    def get(self, index):
        if index < 1:
            raise Exception('Invalid index')

        if index > self.count:
            raise Exception('Index out of range')

        k = 1;
        current = self.head

        while k < index:
            current = current.next
            k += 1

        return current

    def reverse(self):
        if self.is_empty():
            raise Exception('List is empty')

        current = self.head
        prev = None

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def kth_node(self, k):
        p1 = self.head
        p2 = self.head

        for i in range(k):
            if p1 is None:
                return
            p1 = p1.next

        while p1 is not None:
            p1 = p1.next
            p2 = p2.next

        return p2

    def is_empty(self):
        return self.head == None

    def remove_duplicate(self):
        nodes = [];

        prev = None
        current = self.head

        while current is not None:
            if current.item in nodes:
                prev.next = current.next
            else:
                nodes.append(current.item)
                prev = current

            current = current.next
    


def partition(node, x):
    head = node
    tail = node

    while node is not None:
        next = node.next

        if node.item < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node

        node = next
    
    tail.next = None

    return head

def print_list(head):
    current = head

    while current is not None:
        print(current.item)
        current = current.next


def rotate(head):
    for i in range(2):
        prev = None
        current = head

        while current.next is not None:
            prev = current
            current = current.next

        prev.next = None
        current.next = head
        head = current

    return head

ll = LinkedList()

ll.append(3)
ll.append(5)
ll.append(8)
ll.append(5)
ll.append(10)
ll.append(2)
ll.append(1)

print_list(rotate(ll.head))






