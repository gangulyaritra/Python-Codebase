"""
----------------------------
Design Circular Deque.
----------------------------
    1.  https://leetcode.com/problems/design-circular-deque/
    2.  https://www.geeksforgeeks.org/implementation-deque-using-circular-array/
"""

"""
Deque or Double Ended Queue is a generalized version of Queue data structure that allows insert and delete at both ends.

------------------------
Operations on Deque:
------------------------
Mainly, the following four basic operations are performed on deque.
    1.  insertFront(): Adds an item at the front of Deque.
    2.  insertRear(): Adds an item at the rear of Deque.
    3.  deleteFront(): Deletes an item from the front of Deque.
    4.  deleteRear(): Deletes an item from the rear of Deque.

In addition to the above operations, the following operations are also supported.
    1.  getFront(): Gets the front item from the Deque.
    2.  getRear(): Gets the last item from the Deque.
    3.  isEmpty(): Checks whether Deque is empty or not.
    4.  isFull(): Checks whether Deque is full or not.

Time Complexity: O(1)
Space Complexity: O(1)
"""


# Python implementation of Deque using a Circular Queue.
class Deque:
    def __init__(self, size):
        self.array = [0] * 10
        self.front = -1
        self.rear = 0
        self.size = size

    def isFull(self):
        """Checks whether the Deque is full or not."""
        return (
            self.front == 0 and self.rear == self.size - 1
        ) or self.front == self.rear + 1

    def isEmpty(self):
        """Checks whether the Deque is empty or not."""
        return self.front == -1

    def insertfront(self, key):
        """Inserts an element at FRONT."""
        if self.isFull():
            print("Deque is Full.")
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front = self.front - 1
        self.array[self.front] = key

    def insertrear(self, key):
        """Inserts an element at REAR."""
        if self.isFull():
            print("Deque is Full.")
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear = self.rear + 1
        self.array[self.rear] = key

    def deletefront(self):
        """Deletes an element at FRONT."""
        if self.isEmpty():
            print("Deque is Empty.")
            return
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            if self.front == self.size - 1:
                self.front = 0
            else:
                self.front = self.front + 1

    def deleterear(self):
        """Deletes an element at REAR."""
        if self.isEmpty():
            print("Deque is Empty.")
            return
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear = self.rear - 1

    def getFront(self):
        """Returns the FRONT element of Deque."""
        if self.isEmpty():
            print("Deque is Empty.")
            return
        return self.array[self.front]

    def getRear(self):
        """Returns the REAR element of Deque."""
        if self.isEmpty() or self.rear < 0:
            print("Deque is Empty.")
            return
        return self.array[self.rear]

    def DequeSize(self):
        """Returns the current Deque size."""
        return len(self.array)

    def __str__(self):
        """Returns all the elements in Deque."""
        myString = " ".join(str(i) for i in self.array)
        return myString


def display():
    print("******************************")
    print("****** DEQUE OPERATIONS ******")
    print("******************************")
    print("     1. ENQUEUE REAR OPERATION.")
    print("     2. DEQUEUE FRONT OPERATION.")
    print("     3. ENQUEUE FRONT OPERATION.")
    print("     4. DEQUEUE REAR OPERATION.")
    print("     5. PEEK FRONT OPERATION.")
    print("     6. PEEK REAR OPERATION.")
    print("     7. DISPLAY OPERATION.")
    print("     8. QUEUE SIZE.")
    print("     9. EXIT MENU.")
    print("******************************")


if __name__ == "__main__":
    myQueue = Deque(10)  # Initialize Class Object.
    outerloop = True
    innerloop = True
    while outerloop:
        display()
        while innerloop:
            option = int(input("Enter your choice: "))
            if option == 1:
                element = int(input("Enter element to be Inserted: "))
                myQueue.insertrear(element)
            elif option == 2:
                print("Deleted Element is ", myQueue.deletefront())
            elif option == 3:
                element = int(input("Enter element to be Inserted: "))
                myQueue.insertfront(element)
            elif option == 4:
                print("Deleted Element is ", myQueue.deleterear())
            elif option == 5:
                print("Front Element is ", myQueue.getFront())
            elif option == 6:
                print("Front Element is ", myQueue.getRear())
            elif option == 7:
                print("Queue Elements are: ", myQueue.__str__())
            elif option == 8:
                print("Queue Size is: ", myQueue.DequeSize())
            elif option == 9:
                outerloop = False
                innerloop = False
            else:
                print("Invalid Option. Please try again.")
