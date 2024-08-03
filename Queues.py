class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self):
        if(not self.first):
            print('Their are no elements in the queue to print')
        else:
            print('The element/s in the queue are ')
            curr = self.first
            while(curr):
                print(curr.value)
                curr = curr.next
    
    def enqueue(self, value):
        new_node = Node(value)
        if(not self.first):
            self.last = self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        print(f'The element {value} is enqueued')
        self.length += 1
    
    def dequeue(self):
        if(not self.first):
            print('Their are no element/s to dequeue from the queue')
        else:
            if(self.length == 1):
                print('The dequeued element is ', self.first)
                self.last = self.first = None
            else:
                temp = self.first
                self.first = self.first.next
                temp.next = None
                print('The dequeued element is ', temp.value)
            self.length -= 1
    
    def get(self, index):
        if(not self.first):
            print('Their are no elements in the queue to get')
        elif(index < 0 or index >= self.length):
            print(f'Enter the index between 0 and {self.length} to get')
        else:
            curr = self.first
            for i in range(index):
                curr = curr.next
            print(f'At given index {index} the element is ', curr.value)
    
    def queue_length(self):
        print('Length of the queue is ', self.length)


qe = Queue(10)
qe.print_queue()
qe.enqueue(20)
qe.enqueue(30)
qe.print_queue()
qe.queue_length()
qe.dequeue()
qe.print_queue()
qe.queue_length()
qe.enqueue(40)
qe.enqueue(50)
qe.get(2)
qe.print_queue()
qe.queue_length()