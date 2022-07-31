""" **************************************** PRIORITY QUEUE IMPLEMENTATION **************************************** """

"""
A priority queue is a collection of elements such that each element has been assigned a priority and such that the order in which 
elements are deleted and processed comes from the following rules:
    1.  An element of higher priority is processed before any element of lower priority.
    2.  Two elements with the same priority are processed according to the order in which they were added to the queue.
A prototype of a priority queue is a time-sharing system, i.e., programs of high priority are processed first, and programs with the same priority form 
a standard queue. An efficient implementation for the Priority Queue is to use heap, which in turn can be used for sorting purposes called heap sort.
"""

"""
---------------------------------
Definition.
---------------------------------
A priority queue is a special type of queue in which each element is associated with a priority value. Therefore, elements are served 
based on their priority. That is, higher priority elements are served first. However, if elements with the same priority occur, they 
are served according to their order in the queue. The basic operations of a priority queue are inserting, removing, and peeking elements.

---------------------------------
Assigning Priority Value.
---------------------------------
Generally, the value of the element itself is considered for assigning the priority. For example, the element with the highest value 
is considered the highest priority element. However, in other cases, we can assume the element with the lowest value as the highest 
priority element. We can also set priorities according to our needs.

---------------------------------
Priority Queue Vs. Normal Queue.
---------------------------------
In a queue, the first-in-first-out rule is implemented whereas, in a priority queue, the values are removed based on priority. 
The element with the highest priority is removed first.
"""

# Priority Queue Implementation in Python.

# Function to heapify the tree.
def heapify(array, n, i):
    # Find the largest among root, left child, and right child.
    largest = i
    l = (2 * i) + 1
    r = (2 * i) + 2
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    # Swap and continue heapifying if the root is not largest.
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


# Function to insert an element into the tree.
def insertNode(array, item):
    size = len(array)
    if size == 0:
        array.append(item)
    else:
        array.append(item)
        # Heapify the tree.
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


# Function to delete an element from the tree.
def deleteNode(array, item):
    size = len(array)
    i = 0
    for i in range(0, size):
        if item == array[i]:
            break
    # Swap the deleted element with the last element.
    array[i], array[size - 1] = array[size - 1], array[i]
    # Remove the last element.
    array.remove(size - 1)
    # Heapify the tree.
    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


if __name__ == "__main__":
    array = []
    insertNode(array, 3)
    insertNode(array, 4)
    insertNode(array, 9)
    insertNode(array, 5)
    insertNode(array, 2)

    print("Max-Heap array: " + str(array))

    deleteNode(array, 4)
    print("After deleting an element: " + str(array))


"""
-----------------------------------------------------
Priority Queue Implementation using Heap Tree.
-----------------------------------------------------
Priority queue can be implemented using a circular array, a linked list, a heap data structure, or a binary search tree. Among these data structures, 
heap data structure provides an efficient implementation of priority queues. The heap can be represented using an array. This implementation is free 
from the complexities of the circular array and linked list but gets the advantages of simplicities of the array.

Heap trees allow the duplicity of data in them. Elements associated with their priority values are to be stored in form of a heap tree, which can be formed 
based on their priority values. The top priority element that has to be processed first is at the root; so it can be deleted and the heap can be rebuilt to 
get the next element to be processed, and so on.
"""
