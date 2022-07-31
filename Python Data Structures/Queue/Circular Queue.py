""" **************************************** CIRCULAR QUEUE IMPLEMENTATION **************************************** """

"""
A Circular Queue is the extended version of a regular queue where the last element is connected to the first element. 
Therefore, this data structure forms a circle-like structure.

The circular queue solves the major limitation of the normal queue. That is, in a normal queue, after a bit of insertion 
and deletion, there will be non-usable empty space.

Circular Queue works by the process of circular increment, i.e., when we increment the pointer and reach the end of the 
queue, the pointer immediately points to the start of the queue in the next iteration. Here, the circular increment is 
performed by modulo division with the queue size.
"""


class MyCircularQueue(object):
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        """This function checks if the Queue is empty or not and returns True or False."""
        return self.queue == []

    def isFull(self):
        """This function checks if the Queue is full or not and returns True or False."""
        return len(self.queue) == self.size

    def peek(self):
        """This function displays the first element at the Front End of the Queue."""
        if (self.isEmpty() != True) and (self.front != -1 or self.front < self.rear):
            return self.queue[self.front]
        else:
            print("Circular Queue is Empty.")

    def enqueue(self, item):
        """This operation adds an item to the Rear End of the Queue."""
        if self.isFull() == True and ((self.rear + 1) % self.size == self.front):
            print("Circular Queue is Full.")
        elif self.front == -1 or self.rear == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        """This function removes an item from the Front End of the Queue."""
        if (self.isEmpty() != True) and (self.front == -1 or self.rear == -1):
            print("Circular Queue is Empty.")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def __str__(self):
        if (self.isEmpty() != True) and (self.front == -1):
            print("Circular Queue is Empty.")
        elif self.rear >= self.front:
            print("Queue Elements are: ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            print("Queue Elements are: ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


def display():
    print("***************************************")
    print("****** CIRCULAR QUEUE OPERATIONS ******")
    print("******************************")
    print("     1. ENQUEUE OPERATION.")
    print("     2. DEQUEUE OPERATION.")
    print("     3. PEEK OPERATION.")
    print("     4. DISPLAY OPERATION.")
    print("     5. EXIT MENU.")
    print("***************************************")


if __name__ == "__main__":
    myQueue = MyCircularQueue(5)  # Initialize Class Object.
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
                myQueue.__str__()
            elif option == 5:
                outerloop = False
                innerloop = False
            else:
                print("Invalid Option. Please try again.")
