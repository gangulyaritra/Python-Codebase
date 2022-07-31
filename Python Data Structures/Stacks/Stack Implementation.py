""" ********************************************* STACK IMPLEMENTATION ********************************************* """

"""
Stack is an important data structure that stores its elements in an ordered manner.

A Stack is a list of elements in which an element gets inserted or deleted only at one end, called the "top" 
of the stack. Stacks are sometimes known as LIFO (Last In, First Out) lists. As the elements can be added or 
removed only from the top, thus the last element to be added to a stack is the first element to be removed. 
For the array-based implementation of a stack, the time complexity is O(1), and the space complexity of the 
stack with n elements is O(n).

The basic operations associated with stacks are:

    1. Push Operation: The push operation inserts an element into the stack. The new element gets added at the 
                       topmost position of the stack. However, before inserting the element, we must first check 
                       whether the stack is full and elements insertion is possible. An attempt to insert an element
                       into the stack that is already full will cause an error. In this case, a "STACK OVERFLOW" 
                       message gets printed.

    2. Pop Operation: The pop operation deletes the topmost element from the stack. However, before deleting the 
                      element, we must first check whether the stack is empty and elements deletion is possible.
                      An attempt to delete an element from the stack that is already empty will cause an error. 
                      In this case, a "STACK UNDERFLOW" message gets printed.

    3. Peek Operation: The peek operation returns the value of the topmost element of the stack without deleting 
                       it from the stack. However, the peek operation first checks if the stack is empty, i.e., if
                       LIST INDEX = NULL, then an appropriate message is printed, else the topmost element is returned.

Working of Stack Data Structure:

    1. A pointer called "TOP" is used to keep track of the top element in the stack.

    2. During stack initialization, we set the TOP value to -1 to check if the stack is empty by comparing TOP == -1.

    3. While pushing an element, we increment the TOP value and place the new element in the position pointed by the TOP.

    4. While popping an element, we return the element pointed by the TOP and also decrement the TOP value.

    5. Before pushing an element, we check if the stack is already full.

    6. Before popping an element, we check if the stack is already empty.

class Stack:
    def __init__(self):
        self.stack = []
      
    def isEmpty(self):
        return self.stack == []
      
    def push(self, item):
        self.stack.append(item)
      
    def pop(self):
        return self.stack.pop()
      
    def peek(self):
        return self.stack[len(self.stack)-1]
      
    def stackSize(self):
        return len(self.stack)

    def __str__(self):
        myString = ' '.join(str(i) for i in self.stack)
        return myString
"""


class Stack(object):  # Initialize Class.
    # Defined a "class Stack()" and initialize using constructor, i.e., __init__() method, which is going to take the size for our stack.
    def __init__(self, size):
        self.index = (
            []
        )  # Initialize one empty list "index" to store the stack elements inside the list.
        self.size = size  # Initialize Stack Size.

    # isEmpty() Operation checks whether the stack is empty or not, and returns a boolean value, i.e., either True or False.
    def isEmpty(self):
        """Checks whether the stack is empty."""
        return len(self.index) == []

    # isFull() Operation checks whether the stack is full or not, and returns a boolean value, i.e., either True or False.
    def isFull(self):
        """Checks whether the stack is full."""
        return len(self.index) == self.size

    # Push Operation inserts an element to the top of the stack.
    # Push Operation takes one argument as a parameter and inserts that element into the stack.
    def push(self, data):
        """Pushes an element to the top of the stack."""
        if self.isFull() != True:
            self.index.append(data)
            print("Element Inserted.")
        else:
            print("STACK OVERFLOW.")

    # Pop Operation removes or deletes an element from the top of the stack.
    # Pop Operation takes no argument as a parameter and removes the most recently inserted element from the top of the stack.
    def pop(self):
        """Pops out the top element from the stack."""
        if self.isEmpty() != True:
            return self.index.pop()
        else:
            print("STACK UNDERFLOW.")

    # Peek Operation returns the topmost element of the stack.
    # It doesn't pop the element from the stack but returns the element that is at the top of the stack.
    def peek(self):
        """Returns the topmost element from the stack."""
        if self.isEmpty() != True:
            return self.index[-1]
        else:
            print("Stack is Empty.")

    # stackSize() Operation returns the current stack size.
    def stackSize(self):
        """Returns the current stack size."""
        return len(self.index)

    # The below function is used to print the full stack in one line.
    def __str__(self):
        myString = " ".join(str(i) for i in self.index)
        return myString


def display():
    print("******************************")
    print("****** STACK OPERATIONS ******")
    print("******************************")
    print("     1. PUSH OPERATION.")
    print("     2. POP OPERATION.")
    print("     3. PEEK OPERATION.")
    print("     4. DISPLAY OPERATION.")
    print("     5. STACK SIZE.")
    print("     6. EXIT MENU.")
    print("******************************")


if __name__ == "__main__":
    myStack = Stack(12)  # Initialize Class Object.
    outerloop = True
    innerloop = True
    while outerloop:
        display()
        while innerloop:
            option = int(input("Enter your choice: "))
            if option == 1:
                element = int(input("Enter element to be Pushed: "))
                myStack.push(element)
            elif option == 2:
                print("Popped Element is ", myStack.pop())
            elif option == 3:
                print("Topmost Element is ", myStack.peek())
            elif option == 4:
                print("Stack Elements are: ", myStack.__str__())
            elif option == 5:
                print("Stack Size is: ", myStack.stackSize())
            elif option == 6:
                outerloop = False
                innerloop = False
            else:
                print("Invalid Option. Please try again.")
