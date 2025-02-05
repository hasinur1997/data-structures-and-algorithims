class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def get_length(head):
    length = 0

    while head:
        length += 1
        head = head.next

    return length

def get_middle(head):
    length = get_length(head);

    # mid_index = length // 2
    # while mid_index:
    #     head = head.next
    #     mid_index = -1
    #
    # return head.data

    return length

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    print(get_middle(head))


if __name__ == "__main__":
    main()

