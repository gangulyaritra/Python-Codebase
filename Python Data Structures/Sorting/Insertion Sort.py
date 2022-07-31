""" Insertion Sort Tutorials: https://www.programiz.com/dsa/insertion-sort """

"""
Insertion Sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration. 
Insertion Sort works similarly, as we sort cards in our hands in a card game. 

We assume that the first element is already sorted. Therefore, we select the unsorted elements. 
If the unsorted element is greater than the element at first, it gets moved on the right, else to the left. 
In the same way, all other unsorted elements are taken and put in their correct order.

-------------------------------
Working of Insertion Sort.
-------------------------------
Step 1: The first element in the array is assumed to be sorted. Take the second element and store it separately in a "key" variable.

Step 2: Compare the "key" variable with the first element. If the first element is greater than the "key", then the "key" element is 
        placed in front of the first element. Now, the first two elements are sorted.

Step 3: Take the third element and compare it with the elements on the left of it. Place that third element behind the element smaller 
        than it. If there is no element smaller than it, then place it at the beginning of the array.

Step 4: Similarly, place every unsorted element at its correct position.

-------------------------
Complexity Analysis:
-------------------------
1.  Best:       O(n)
2.  Worst:      O(n^2)
3.  Average:    O(n^2)

Space Complexity:    O(1)
"""

# Insertion Sort in Python.
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # Compare key with each element on the left of it until an element smaller than it is found.
        # For descending order, change key < array[j] to key > array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        # Place key after the element just smaller than it.
        array[j + 1] = key


if __name__ == "__main__":
    array = []
    size = int(input("Enter the number of elements: "))
    for i in range(size):
        ele = int(input("Enter the elements: "))
        array.append(ele)
    print("Original List is ", array)
    insertionSort(array)
    print("Sorted List is ", array)
