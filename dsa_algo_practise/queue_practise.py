class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return "queue meh kuch nahi hai"
        temp = self.front
        self.front = self.front.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.is_empty():
            return "queue meh kuch nahi hai"
        return self.front.data
    
    def is_empty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def print_queue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Create a queue
mera_queue = Queue()
mera_queue.enqueue('A')
mera_queue.enqueue('B')
mera_queue.enqueue('C')
print("Queue: ", end="")
mera_queue.print_queue()

print("Dequeue: ", mera_queue.dequeue())
print("Peek: ", mera_queue.peek())
print("isEmpty: ", mera_queue.is_empty())
print("Size: ", mera_queue.size())