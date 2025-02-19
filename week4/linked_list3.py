class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)

        # If no head Node exists
        if self.head is None:
            self.head = new_node
            print(f"Head Node created: {self.head.value}")
            return
        
        #Traverse the linked-list until tail and attach
        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print(f"Appended new Node with value: {node.next.value}")