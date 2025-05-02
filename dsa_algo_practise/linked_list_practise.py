class linkedList():
    def __init__(self):
        pass

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def singly_linked_list(self, Node):
        self.node1 = Node(3)
        self.node2 = Node(5)
        self.node3 = Node(12)
        self.node4 = Node(2)

        self.node1.next = self.node2
        self.node2.next = self.node3
        self.node3.next = self.node4

        currentNode = self.node1
        while currentNode:
            print(currentNode.data, end="->")
            currentNode = currentNode.next
        print("null")
        return
    
    def doubly_linked_list(self, Node):
        self.node1.next = self.node2

        self.node2.prev = self.node1
        self.node2.next = self.node3

        self.node3.prev = self.node2
        self.node3.next = self.node3

        self.node4.prev = self.node3

    def traversing_forward(self):
        currentNode = self.node1
        while currentNode:
            print(currentNode.data, end="-> ")
            currentNode = currentNode.next
        print("null")

    def traversing_backward(self):
        currentNode = self.node4
        while currentNode:
            print(currentNode.data, end="-> ")
            currentNode = currentNode.next
        print("null")

    def circular_singly_linked_list(self):
        self.node1.next = self.node2
        self.node2.next = self.node3
        self.node3.next = self.node4
        self.node4.next = self.node1

    # traversing_forward(circular_singly_linked_list)
        # making list circular
        currentNode = self.node1
        startNode = self.node1
        print(currentNode.data, end=" -> ") 
        currentNode = currentNode.next 

        while currentNode != startNode:
            print(currentNode.data, end="-> ")
            currentNode = currentNode.next

    def circular_doubly_linked_list(self):
        self.node1.next = next.node2
        self.node1.prev = next.node4

        self.node2.prev = next.node1
        self.node2.next = next.node3

        self.node3.prev = next.node2
        self.node3.next = next.node4

        self.node4.prev = next.node3
        self.node4.next = next.node1

    def traverse_and_print(self, head):
        currentNode = head
        while currentNode:
            print(currentNode.data, end="-> ")
            currentNode = currentNode.next
        print("null")

    def delete_specific_node(self, head, node_to_delete):
        if head == node_to_delete:
            return head.next
        
        currentNode = head
        while currentNode.next and currentNode.next != node_to_delete:
            currentNode = currentNode.next

        currentNode.next = currentNode.next.next

        return head
    
    def insert_node_at_position(self, head, new_node, position):
        if position == 1:
            new_node.next = head
            return new_node
        
        current_node = head
        for _ in range(position - 2):
            if current_node is None:
                break
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node
        return head
    
     
