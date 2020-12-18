from collections import deque

class Stack:
    
    def __init__(self):
        self.stack=deque()
    
    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def empty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        print(self.stack)
    

s=Stack()
print(s.empty())
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
print(s.display())
s.pop()
s.pop()
print(s.display())
print(s.peek())

