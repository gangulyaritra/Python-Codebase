""" ************************************ LINKED LIST IMPLEMENTATION OF STACK ************************************ """

"""
We can represent a stack using a linked list. In a stack, the push and pop operations are performed at one end called the top. 
We can perform similar operations at one end of the linked list by using the top pointer. The main advantage of using a linked 
list over arrays is that it is possible to implement a stack that can shrink or grow as much as needed. Using an array will put 
a restriction on the maximum capacity, which can lead to stack overflow. In linked list implementation of stack, each new node 
will be dynamically allocated. So stack overflow is not possible.

We have seen how a stack is created using an array. Creating a stack using arrays is easy, but the drawback is that the array 
must be declared to have some fixed size. If the size of the stack is small, or we know its maximum size in advance, then the 
array implementation of the stack gives an efficient implementation. But if the array size cannot be determined in advance, then 
the other alternative, i.e., linked list representation, is used. 

In a linked stack, every node has two parts, i.e., one that stores data and another that stores the address of the next node.

We have seen how a stack is created using an array. Creating a stack using arrays is easy, but the drawback is 
that the array must be declared to have some fixed size. If the size of the stack is small, or we know its maximum 
size in advance, then the array implementation of the stack gives an efficient implementation. But if the array 
size cannot be determined in advance, then the other alternative, i.e., linked list representation, is used.

For the linked list-based implementation of a stack, the time complexity is O(1), and the space complexity of the stack with n elements is O(n).
"""


class Node:
    # Class to create nodes of linked list constructor initializes node automatically.
    def __init__(self, key):
        self.key = key
        self.next = None


class Stack:
    def __init__(self):
        self.top = None  # Initialize Stack TOP.

    # isEmpty() Operation checks whether the stack is empty or not, and returns a boolean value, i.e., either True or False.
    def isEmpty(self):
        """Checks whether the stack is empty."""
        if self.top == None:
            return True
        else:
            return False

    # Push Operation inserts an element to the top of the stack.
    # Push Operation takes one argument as a parameter and inserts that element into the stack.
    def push(self, data):
        """Pushes an element to the top of the stack."""
        if self.top == None:
            self.top = Node(data)
            print("Element Inserted.")
        else:
            newnode = Node(data)
            newnode.next = self.top
            self.top = newnode  # Update top pointer.
            print("Element Inserted.")

    # Peek Operation returns the topmost element of the stack.
    # It doesn't pop the element from the stack but returns the element that is at the top of the stack.
    def peek(self):
        """Returns the topmost element from the stack."""
        if self.isEmpty():
            print("Stack is Empty.")
        else:
            return self.top.key

    # Pop Operation removes or deletes an element from the top of the stack.
    # Pop Operation takes no argument as a parameter and removes the most recently inserted element from the top of the stack.
    def pop(self):
        """Pops out the top element from the stack."""
        if self.isEmpty():
            print("STACK UNDERFLOW.")
        else:
            # Removes the top node and makes the preceding one the new top.
            print("Popped Element is", self.top.key)
            self.top = self.top.next

    # The below function is used to print the full stack in one line.
    def display(self):
        iternode = self.top
        if self.isEmpty():
            print("STACK UNDERFLOW.")
        else:
            while iternode != None:
                print(iternode.key, "<-", end=" ")
                iternode = iternode.next
            print("\n")
            return


def menu():
    print("******************************")
    print("****** STACK OPERATIONS ******")
    print("******************************")
    print("     1. PUSH OPERATION.")
    print("     2. POP OPERATION.")
    print("     3. PEEK OPERATION.")
    print("     4. DISPLAY OPERATION.")
    print("     5. EXIT MENU.")
    print("******************************")


if __name__ == "__main__":
    MyStack = Stack()  # Initialize Class Object.
    outerloop = True
    innerloop = True
    while outerloop:
        menu()
        while innerloop:
            option = int(input("Enter your choice: "))
            if option == 1:
                element = int(input("Enter element to be Pushed: "))
                MyStack.push(element)
            elif option == 2:
                MyStack.pop()
            elif option == 3:
                print("Topmost Element is ", MyStack.peek())
            elif option == 4:
                print("Stack Elements are: ")
                MyStack.display()
            elif option == 5:
                outerloop = False
                innerloop = False
            else:
                print("Invalid Option. Please try again.")
