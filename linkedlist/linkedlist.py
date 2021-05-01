from data_structure.linkedlist.node import Node


# Class Linked List
class LinkedList:

    # Initialize
    def __init__(self):
        self.head = None
        self.counter = 0

    # Add node top of the list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.counter = self.counter + 1
        else:
            current_node = self.head

            while current_node.next is not None:
                self.counter = self.counter + 1
                current_node = current_node.next

            current_node.next = new_node

    # Add node at the end of the list
    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.counter = self.counter + 1
            self.head = new_node
        else:
            self.counter = self.counter + 1
            temp = self.head
            self.head = new_node
            new_node.next = temp

    # Insert node at any position of the list
    def insert(self, insert_at, data):
        new_node = Node(data)

        if self.head is None:
            print("The list is empty")
        elif insert_at == 0 or insert_at == 1:
            temp = self.head
            self.head = new_node
            new_node.next = temp
        else:
            destination = insert_at - 1
            current_position = 1
            current_node = self.head

            while current_position is not destination:
                current_position = current_position + 1
                current_node = current_node.next

            temp = current_node.next
            current_node.next = new_node
            new_node.next = temp

    # Update node at any position
    def update(self, position, data):
        if self.head is None:
            print("The list is empty")

        else:
            current_node = self.head
            current_position = 1

            while current_position is not position:
                current_position = current_position + 1
                current_node = current_node.next
            current_node.data = data

    # Remove node from the end of the list
    def pop(self):
        if self.head is None:
            print("The list is empty. Nothing to delete")
        else:
            if self.head.next is None:
                self.head = None
                return
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next

            current_node.next = None

    # Remove node from top of the list
    def shift(self):
        if self.head is None:
            print("The list is empty")
        else:
            self.head = self.head.next

    # Remove node from at any position of the list
    def remove(self, position):
        if self.head is None:
            print("The list is empty. Nothing to print")
        elif position == 1:
            self.shift()
        elif position == self.counter:
            self.pop()
        else:
            current_position = 1
            destination = position - 1

            current_node = self.head
            while current_position is not destination:
                current_node = current_node.next
                current_position = current_position + 1

            temp = current_node.next.next
            current_node.next = temp

    # Remove duplicate nodes from the list
    def remove_duplicates(self):

        if self.head is None:
            return None

        current_node = self.head
        has = set()
        has.add(self.head.data)

        while current_node.next is not None:
            if current_node.next.data in has:
                current_node.next = current_node.next.next
            else:
                has.add(current_node.next.data)
                current_node = current_node.next

    # Get total numbers of node of the list
    def count(self):
        return self.counter

    # Get minimum value from the list
    def min(self):
        if self.head is None:
            return None

        current_node = self.head
        min_value = current_node.data

        while current_node is not None:
            if current_node.data < min_value:
                min_value = current_node.data
            current_node = current_node.next

        return min_value

    # Get the maximum value from the list
    def max(self):
        if self.head is None:
            return None

        current_node = self.head
        max_value = current_node.data

        while current_node is not None:
            if current_node.data > max_value:
                max_value = current_node.data
            current_node = current_node.next

        return max_value

    # Get the first node value
    def first(self):
        if self.head is None:
            return None
        return self.head.data

    # Get the value of last node
    def last(self):
        if self.head is None:
            return None

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        return current_node.data

    # Sort the list
    def sort(self):
        if self.head is None:
            print("The list is empty")
            return

        current_node = self.head

        while current_node is not None:
            index = current_node.next

            while index is not None:
                if current_node.data > index.data:
                    temp = current_node.data
                    current_node.data = index.data
                    index.data = temp

                index = index.next
            current_node = current_node.next

    # Find node using the value
    def find(self, item):
        if self.head is None:
            print("This is empty, Nothing to search")
            return
        else:
            current_node = self.head
            found_item = None
            while current_node is not None:
                if item == current_node.data:
                    found_item = current_node
                    break
                current_node = current_node.next

        return found_item

    # Get the data at the respected position
    def get(self, position):
        if self.head is None:
            return None

        current = self.head
        result = None
        index = 1

        while current is not None:
            if index == position:
                result = current
            current = current.next
            index = index + 1

        return result.data

    # Get the item from the position of the tail
    def get_from_tail(self, position):
        if self.head is None:
            return None

        counter = 0
        current_node = self.head

        while current_node is not None:
            counter = counter + 1
            current_node = current_node.next

        current_node = self.head
        for i in range(0, counter - position):
            current_node = current_node.next

        return current_node.data

    # Print the list
    def display(self):
        if self.head is None:
            print("The list is empty, Nothing to print")
        else:
            current_node = self.head

            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next
