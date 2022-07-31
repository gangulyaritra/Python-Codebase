""" ************************************ LINKED LIST IMPLEMENTATION OF QUEUE ************************************ """


class Node:
    """Class to create nodes of linked list constructor initializes node automatically."""
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        """Initialize Queue FRONT & REAR."""
        self.front = self.rear = None

    def isEmpty(self):
        """This function checks if the Queue is empty or not and returns True or False."""
        return self.front == None

    def EnQueue(self, item):
        """Method to add an item to the Queue."""
        temp = Node(item)
        if self.rear == None:
            self.front = self.rear = temp
            print("Element Inserted.")
        else:
            self.rear.next = temp
            self.rear = temp
            print("Element Inserted.")

    def DeQueue(self):
        """Method to remove an item from the Queue."""
        if self.isEmpty() == True:
            self.rear = None
            print("Queue is Empty.")
        else:
            temp = self.front
            self.front = temp.next
            return temp.data

    def peek(self):
        """Returns the topmost element from the Queue."""
        if self.isEmpty() == True:
            self.rear = None
            print("Queue is Empty.")
        else:
            return self.front.data

    def __str__(self):
        """The below function is used to print the full Queue in one line."""
        iternode = self.front
        if self.isEmpty() == True:
            print("Queue is Empty.")
        else:
            print("Queue Elements are: ")
            while iternode != None:
                print(iternode.data, "<-", end=" ")
                iternode = iternode.next
            return


def menu():
    print("******************************")
    print("****** QUEUE OPERATIONS ******")
    print("******************************")
    print("     1. ENQUEUE OPERATION.")
    print("     2. DEQUEUE OPERATION.")
    print("     3. PEEK OPERATION.")
    print("     4. DISPLAY OPERATION.")
    print("     5. EXIT MENU.")
    print("******************************")


if __name__ == "__main__":
    myQueue = Queue()  # Initialize Class Object.
    outerloop = True
    innerloop = True
    while outerloop:
        menu()
        while innerloop:
            option = int(input("Enter your choice: "))
            if option == 1:
                element = int(input("Enter element to be Inserted: "))
                myQueue.EnQueue(element)
            elif option == 2:
                print("Deleted Element is ", myQueue.DeQueue())
            elif option == 3:
                print("Front Element is ", myQueue.peek())
            elif option == 4:
                myQueue.__str__()
            elif option == 5:
                outerloop = False
                innerloop = False
            else:
                print("Invalid Option. Please try again.")
