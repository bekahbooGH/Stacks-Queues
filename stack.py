class Stack:
  def __init__(self):
    self.data = []
    
  def __repr__(self):
    return f"Stack bottom {self.data} top"

  def push(self, x):
    self.data.append(x)

  def empty(self):
    return len(self.data) == 0

  def pop(self):
    return self.data.pop()

  def peek(self):
    return self.data[-1]

# Stack:
#push: append to python list
#pop: pop from python list - takes it from the back, which in a stack is the top element
#peek: return list[-1] because that's the last element, and in a stack it's the top element
#empty: check if len(list) == 0

s = Stack()

s = Stack()

s.push("apple")
s.push("mango")
s.push("blueberries")
s.push("cherries")

s.empty()

s.pop()

s.peek()