""" Queue using Stacks: https://www.geeksforgeeks.org/queue-using-stacks/ """

"""
-------------------------------------------------
Method 1: (By making enQueue operation costly)
-------------------------------------------------
This method makes sure that the oldest entered element is always at the top of Stack 1, 
so that the deQueue operation just pops from Stack 1. To put the element at top of Stack 1, Stack 2 is used.

Time Complexity is O(n): Use of the Stack for storing values.
"""


class Queue1:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, item):
        """Time Complexity is O(n): In the worst case, we have to empty the whole of Stack 1 into Stack 2."""
        # While Stack 1 is NOT Empty, PUSH all elements from Stack 1 to Stack 2.
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        # PUSH Item to Stack 1 (assuming the size of Stacks is unlimited).
        self.s1.append(item)
        # PUSH all elements back to Stack 1 from Stack 2.
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def deQueue(self):
        """Time Complexity is O(1): Same as the POP operation in the Stack."""
        if len(self.s1) == 0:
            print("Queue is Empty.")
        # POP out the last element inserted into Stack 1.
        temp = self.s1[-1]
        self.s1.pop()
        return temp


"""
-------------------------------------------------
Method 2: (By making deQueue operation costly)
-------------------------------------------------
In this method, using the enQueue operation, the new element is entered at the top of Stack 1.
In the deQueue operation, if Stack 2 is empty, then all the elements are moved to Stack 2 from Stack 1, 
and finally, the top of Stack 2 is returned.

Method 2 is better than Method 1.

Method 1 moves all the elements twice in enQueue operation, while Method 2 (in the deQueue operation) 
moves the elements once and moves the elements, only if Stack 2 is empty.

Time Complexity is O(n): Use of the Stack for storing values.
"""


class Queue2:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, item):
        """Time Complexity is O(1): Same as the PUSH operation in the Stack."""
        # PUSH Item to Stack 1 (assuming the size of Stacks is unlimited).
        self.s1.append(item)

    def deQueue(self):
        """Time Complexity is O(n)"""
        # If both Stacks are Empty, then Stack is Empty.
        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Queue is Empty.")
        # If Stack 2 is Empty
        # While Stack 1 is not empty, PUSH everything from Stack 1 to Stack 2.
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            # POP the element from Stack 2 and return it.
            return self.s2.pop()
        else:
            # POP the element from Stack 2 and return it.
            return self.s2.pop()


"""
-------------------------------------------------
Method 3: (By making enQueue operation costly)
-------------------------------------------------
A Queue can also be implemented using one user Stack and one Function Call Stack. Below is modified Method 2 
where recursion (or Function Call Stack) is used to implement Queue using only one user-defined Stack.

Time Complexity is O(n): Use of the Stack for storing values.
"""


class Queue:
    def __init__(self):
        self.stack = []

    def enQueue(self, item):
        """Time Complexity is O(1): Same as the PUSH operation in the Stack."""
        # PUSH Item to Stack (assuming the size of Stacks is unlimited).
        self.stack.append(item)

    def deQueue(self):
        """Time Complexity is O(n)"""
        # If Stack is Empty.
        if len(self.stack) <= 0:
            print("Queue is Empty.")
        # If Stack has one element then return it.
        temp = self.stack[len(self.stack) - 1]
        self.stack.pop()
        if len(self.stack) <= 0:
            return temp
        # Recursively POP all elements from the Stack, store the popped item in a variable
        # "temp" and then PUSH the "temp" back to the Stack and return "temp".
        item = self.deQueue()

        self.stack.append(temp)

        return item


# Main Code.
if __name__ == "__main__":
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
