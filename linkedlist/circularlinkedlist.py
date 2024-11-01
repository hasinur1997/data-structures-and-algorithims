from data_structure.linkedlist.node import Node


# Circular Linked List Class
class CircularLinkedList:
    # Initialize
    def __init__(self):
        self.head = None

    # Add node at the end of the list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head

            while current_node.next != self.head:
                current_node = current_node.next

            current_node.next = new_node

        new_node.next = self.head

    # Display the list
    def display(self):
        if self.head is None:
            print("The list is empty. Nothing to display")
        else:
            concurrent_node = self.head

            while True:
                print(concurrent_node.data)
                concurrent_node = concurrent_node.next

                if concurrent_node == self.head:
                    break
