""" Heap Sort Tutorials: https://www.programiz.com/dsa/heap-sort """

"""
A heapsort algorithm works by first organizing the data into a special type of binary tree called a heap.
A list of data can be sorted either in ascending order or in descending order using a heap tree.
It does this with the following steps:

    1.  Build a heap tree with the given set of data.
    2.  a.  Remove the topmost item (the largest) and replace it with the last element in the heap.
        b.  Re-heapify the complete binary tree.
        c.  Place the deleted node in the output.
    3.  Continue Step 2 until the heap tree is empty.

------------------------
Working of Heap Sort.
------------------------
1.  Since the tree satisfies the Max-Heap property, therefore the largest item is stored at the root node.
2.  Swap: Remove the root element and put it at the end of the array (nth position). Put the last item of 
    the tree (heap) at the vacant place.
3.  Remove: Reduce the size of the heap by 1.
4.  Heapify: Heapify the root element again so that we have the highest element at root.
5.  The process is repeated until all the items on the list are sorted.

-------------------------
Complexity Analysis:
-------------------------
Heap Sort has O(n log n) time complexities for all the cases (best case, average case, and worst case).
    Time Complexity:    O(n log n)
    Space Complexity:   O(1)

Heap Sort algorithm sorts the elements a[n]. Heap Sort rearranges them in place in non-decreasing order.
First, transform the elements into a heap.
"""


# Heap Sort in Python.
def heapify(array, n, i):
    # Find the largest among root and children.
    largest = i
    l = (2 * i) + 1
    r = (2 * i) + 2
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    # If the root is not largest, swap with largest and continue heapifying.
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapSort(array):
    n = len(array)
    # Build Max Heap.
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        # Swap.
        array[i], array[0] = array[0], array[i]
        # Heapify root element.
        heapify(array, i, 0)


if __name__ == "__main__":
    array = []
    size = int(input("Enter the number of elements: "))
    for i in range(size):
        ele = int(input("Enter the elements: "))
        array.append(ele)
    print("Original List is ", array)
    heapSort(array)
    print("Sorted array is ", array)
