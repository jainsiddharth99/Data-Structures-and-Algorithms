from collections import deque

class Queue:
    
    def __init__(self):
        self.queue=deque()
    
    def enqueue(self,data):
        self.queue.appendleft(data)
        
    def dequeue(self):
        return self.queue.pop()
    
    def peek(self):
        return self.queue[0]
    
    def empty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        print(self.queue)
    

q=Queue()
print(q.empty())
q.enqueue(1)
q.enqueue(3)
q.enqueue(5)
q.enqueue(7)
q.enqueue(9)
print(q.display())
q.dequeue()
print(q.display())
q.dequeue()
print(q.display())
q.enqueue(10)
print(q.peek())
print(q.display())