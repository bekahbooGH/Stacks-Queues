class MyQueue:
    def __init__(self):
        """Initialize your data structure here."""
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        """Push element x to the back of queue."""
        while not self.stack2.empty():
          self.stack1.push(self.stack2.pop())
        self.stack1.push(x)
        
    def pop(self) -> int:
        """Removes the element from in front of queue and returns that element."""
        self.peek()
        return self.stack2.pop()

    def pop2(self) -> int:
        """Removes the element from in front of queue and returns that element."""
        while not self.stack1.empty():
          self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
        
    def peek(self) -> int:
        """Get the front element."""
        while not self.stack1.empty():
          self.stack2.push(self.stack1.pop())
        return self.stack2.peek()
        
    def empty(self) -> bool:
        """Returns whether the queue is empty."""
        return self.stack1.empty() and self.stack2.empty()

my_queue = MyQueue()  