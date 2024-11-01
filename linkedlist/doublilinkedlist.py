from data_structure.linkedlist.node import Node


# Class Doubly Linked List
class DoublyLinkedList:
    # Initialize
    def __init__(self):
        self.head = None
        self.tail = None

    # Add node end of the list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Add node top of the list
    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node

    # Insert an item to the appropriate location
    def sorted_insert(self, item):
        new_node = Node(item)
        current_node = self.head

        while current_node is not None:
            if current_node.data >= item:
                new_prev = current_node.prev
                current_node.prev.next = new_node
                new_node.next = current_node
                new_node.prev = new_prev
                return

            current_node = current_node.next

    # Reverse doubly linked list
    def reverse(self):
        if self.head is None:
            return None
        else:
            current_node = self.head

            while current_node is not None:
                # Exchange node
                next_node = current_node.next
                current_node.next = current_node.prev
                current_node.prev = next_node

                current_node = next_node

            # Exchange node between head and tail
            current = self.head
            self.head = self.tail
            self.tail = current

    # Display the list
    def display(self):
        if self.head is None:
            print("The list is empty. Nothing to display")

        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next
