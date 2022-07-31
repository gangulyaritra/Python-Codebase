""" ********************************************* QUEUE IMPLEMENTATION ********************************************* """

"""
Queue is an important data structure that stores its elements in an ordered manner.

A Queue is another special kind of data structure, where items are inserted at one end called the REAR and 
deleted at the other end called the FRONT. A queue is known as "FIFO", or "First-In-First-Out" data structure.

The operations for a Queue are analogous to those of a Stack, the difference is that the deletion goes at the 
start of the list rather than the end. We shall use the following operations on Queues:
    1.  Enqueue: which inserts an element at the end of the Queue.
    2.  Dequeue: which deletes an element at the start of the Queue.

To create a Queue, we require a one-dimensional array Q(1:N) and two variables FRONT and REAR. Thus, FRONT = REAR, 
if and only if there are no elements in the Queue. The initial condition then is FRONT = REAR = -1.

1.  If we want to insert an element from the Queue, then the value of REAR will be incremented.
    Insertions are done from only the REAR end of the Queue.

2.  If we want to delete an element from the Queue, then the value of FRONT will be incremented.
    Deletions are done from only the FRONT end of the Queue.
"""


class Queue(object):
    def __init__(self, size):
        self.queue = []
        self.front = -1
        self.rear = -1
        self.size = size

    def isEmpty(self):
        """This function checks if the Queue is empty or not and returns True or False."""
        return self.queue == []

    def isFull(self):
        """This function checks if the Queue is full or not and returns True or False."""
        return len(self.queue[self.front : self.rear]) == self.size

    def peek(self):
        """This function displays the first element at the Front End of the Queue."""
        if (self.isEmpty() != True) and (self.front != -1 or self.front < self.rear):
            return self.queue[self.front]
        else:
            print("Queue is Empty.")

    def enqueue(self, item):
        """This operation adds an item to the Rear End of the Queue."""
        if self.isFull() != True and self.size > len(
            self.queue[self.front : self.rear]
        ):
            if self.front == -1 and self.rear == -1:
                self.front = 0
                self.rear = 0
                self.queue.append(item)
            else:
                self.rear += 1
                self.queue.append(item)
        else:
            print("Queue is Full.")

    def dequeue(self):
        """This function removes an item from the Front End of the Queue."""
        if (self.isEmpty() != True) and (self.front != -1 or self.front < self.rear):
            val = self.queue[self.front]
            self.front += 1
            if self.front > self.rear:
                self.front = -1
                self.rear = -1
            return val
        else:
            print("Queue is Empty.")

    def QueueSize(self):
        """Returns the current Queue size."""
        return len(self.queue[self.front : self.rear]) + 1

    def __str__(self):
        myString = " ".join(str(i) for i in self.queue[self.front : self.rear + 1])
        return myString


def display():
    print("******************************")
    print("****** QUEUE OPERATIONS ******")
    print("******************************")
    print("     1. ENQUEUE OPERATION.")
    print("     2. DEQUEUE OPERATION.")
    print("     3. PEEK OPERATION.")
    print("     4. DISPLAY OPERATION.")
    print("     5. QUEUE SIZE.")
    print("     6. EXIT MENU.")
    print("******************************")


if __name__ == "__main__":
    myQueue = Queue(7)  # Initialize Class Object.
    outerloop = True
    innerloop = True
    while outerloop:
        display()
        while innerloop:
            option = int(input("Enter your choice: "))
            if option == 1:
                element = int(input("Enter element to be Inserted: "))
                myQueue.enqueue(element)
            elif option == 2:
                print("Deleted Element is ", myQueue.dequeue())
            elif option == 3:
                print("Front Element is ", myQueue.peek())
            elif option == 4:
                print("Queue Elements are: ", myQueue.__str__())
            elif option == 5:
                print("Queue Size is: ", myQueue.QueueSize())
            elif option == 6:
                outerloop = False
                innerloop = False
            else:
                print("Invalid Option. Please try again.")
