""" Stack using Queues: https://www.geeksforgeeks.org/implement-stack-using-queue/ """

"""
-------------------------------------------------
Method 1: (By making PUSH operation costly)
-------------------------------------------------
This method makes sure that the newly entered element is always at the front of q1, so that POP 
operation just dequeues from "q1". "q2" is used to put every new element at front of "q1".

Time Complexity is O(n): Use of the Queue for storing values.
"""

from queue import Queue


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.curr_size = 0

    def push(self, item):
        """Time Complexity is O(n)."""
        self.curr_size += 1
        # Enqueue item to q2.
        self.q2.put(item)
        # One by one dequeue everything from q1 and enqueue to q2.
        while not self.q1.empty():
            self.q2.put(self.q1.queue[0])
            self.q1.get()
        # Swap the names of q1 and q2.
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def pop(self):
        """Time Complexity is O(1)."""
        if self.q1.empty():
            print("Stack UnderFlow.")
        # POP the top item from q1 and return it.
        self.q1.get()
        self.curr_size -= 1

    def peek(self):
        if self.q1.empty():
            print("Stack UnderFlow.")
        return self.q1.queue[0]

    def size(self):
        return self.curr_size


# Main Code.
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print("Current Size of Stack: ", s.size())
    print(s.peek())
    s.pop()
    print(s.peek())
    s.pop()
    print(s.peek())

    print("Current Size of Stack: ", s.size())
