""" ********************************************* DEQUE IMPLEMENTATION ********************************************* """

"""
A simple Queue inserts an item at one end called REAR and deletes an item from another end called FRONT.

DEQUE or Double-ended Queue is an extension of the queue, which provides insertion and deletion 
of items at both ends of the queue. A deque provides four operations.

1.  enqueue_front: insert an element at front.
2.  dequeue_front: delete an element at front.
3.  enqueue_rear: insert element at rear.
4.  dequeue_rear: delete element at rear.

There are two variations of the deque. They are:
    1.  Input Restricted Deque (IRD)
    2.  Output Restricted Deque (ORD)

An Input restricted deque is a deque, which allows insertions at one end but allows deletions at both ends of the list.

An Output restricted deque is a deque, which allows deletions at one end but allows insertions at both ends of the list.
"""


class Deque:
    def __init__(self):
        self.deque = []

    def isEmpty(self):
        """This function checks if the Deque is empty or not and returns True or False."""
        return self.deque == []

    def peek(self):
        """This function displays the first element at the Front End of the Deque."""
        if self.isEmpty() != True:
            return self.deque[0]
        else:
            print("Deque is Empty.")

    def enqueue_rear(self, item):
        """This function adds an item to the Rear End of the Deque."""
        self.deque.append(item)

    def enqueue_front(self, item):
        """This function adds an item to the Front End of the Deque."""
        self.deque.insert(0, item)

    def dequeue_front(self):
        """This function removes an item from the Front End of the Deque."""
        if self.isEmpty() != True:
            val = self.deque[0]
            del self.deque[0]
            return val
        else:
            print("Deque is Empty.")

    def dequeue_rear(self):
        """This function removes an item from the Rear End of the Deque."""
        if self.isEmpty() != True:
            val = self.deque[-1]
            del self.deque[-1]
            return val
        else:
            print("Deque is Empty.")

    def DequeSize(self):
        """Returns the current Deque size."""
        return len(self.deque)

    def __str__(self):
        myString = " ".join(str(i) for i in self.deque)
        return myString


def display():
    print("******************************")
    print("****** DEQUE OPERATIONS ******")
    print("******************************")
    print("     1. ENQUEUE REAR OPERATION.")
    print("     2. DEQUEUE FRONT OPERATION.")
    print("     3. ENQUEUE FRONT OPERATION.")
    print("     4. DEQUEUE REAR OPERATION.")
    print("     5. PEEK OPERATION.")
    print("     6. DISPLAY OPERATION.")
    print("     7. QUEUE SIZE.")
    print("     8. EXIT MENU.")
    print("******************************")


if __name__ == "__main__":
    myQueue = Deque()  # Initialize Class Object.
    outerloop = True
    innerloop = True
    while outerloop:
        display()
        while innerloop:
            option = int(input("Enter your choice: "))
            if option == 1:
                element = int(input("Enter element to be Inserted: "))
                myQueue.enqueue_rear(element)
            elif option == 2:
                print("Deleted Element is ", myQueue.dequeue_front())
            elif option == 3:
                element = int(input("Enter element to be Inserted: "))
                myQueue.enqueue_front(element)
            elif option == 4:
                print("Deleted Element is ", myQueue.dequeue_rear())
            elif option == 5:
                print("Front Element is ", myQueue.peek())
            elif option == 6:
                print("Queue Elements are: ", myQueue.__str__())
            elif option == 7:
                print("Queue Size is: ", myQueue.DequeSize())
            elif option == 8:
                outerloop = False
                innerloop = False
            else:
                print("Invalid Option. Please try again.")
