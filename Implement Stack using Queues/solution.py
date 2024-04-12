class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        if not self.head:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next

    def pop(self) -> int:
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self) -> int:
        return self.head.val if self.head else None

    def empty(self) -> bool:
        return self.head is None

class MyStack:

    def __init__(self):
        self.q1 = MyQueue()
        self.q2 = MyQueue()

    def push(self, x: int) -> None:
        self.q1.push(x)
        while not self.q2.empty():
            self.q1.push(self.q2.pop())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q2.pop()

    def top(self) -> int:
        return self.q2.peek()

    def empty(self) -> bool:
        return self.q2.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
