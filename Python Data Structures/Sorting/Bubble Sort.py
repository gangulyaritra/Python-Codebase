""" Bubble Sort Tutorials: https://www.programiz.com/dsa/bubble-sort """

"""
Bubble Sort is a sorting algorithm that compares two adjacent elements and swaps them until they are not in the intended order.

The bubble sort is easy to understand and program. The basic idea of bubble sort is to pass through 
the file sequentially several times. In each pass, we compare each element in the file with its successor, 
i.e., X[i] with X[i+1], and interchange two elements when they are not in proper order. We will illustrate 
this sorting technique by taking a specific example. Bubble Sort is also called an exchange sort.

--------------------------
Working of Bubble Sort:
--------------------------

A. First Iteration (Compare and Swap):
    1. Bubble Sort starts with the first two elements, comparing them to check which one is greater.
    2. If the first element is greater than the second element, they get swapped.
    3. Now, compare the second and the third elements. Swap them if they are not in order.
    4. The above process goes on until the last element.

B. Remaining Iteration:
    1. The same process goes on for the remaining iterations.
    2. After each iteration, the largest element among the unsorted elements is placed at the end.
    3. In each iteration, the comparison takes place up to the last unsorted element.
    4. The array is sorted when all the unsorted elements are placed at their correct positions.

Consider an array, array = [5, 1, 4, 2, 8]. We are trying to sort the elements in ascending order.

First Pass:
    1. [5, 1, 4, 2, 8] -> [1, 5, 4, 2, 8]; Swap 5 and 1 since 5 > 1.
    2. [1, 5, 4, 2, 8] -> [1, 4, 5, 2, 8]; Swap 5 and 4 since 5 > 4.
    3. [1, 4, 5, 2, 8] -> [1, 4, 2, 5, 8]; Swap 5 and 2 since 5 > 2.
    4. [1, 4, 2, 5, 8] -> [1, 4, 2, 5, 8]; No Swapping since 8 > 5.

Second Pass:
    1. [1, 4, 2, 5, 8] -> [1, 4, 2, 5, 8]; No Swapping since 4 > 1.
    2. [1, 4, 2, 5, 8] -> [1, 2, 4, 5, 8]; Swap 4 and 2 since 4 > 2.
    3. [1, 2, 4, 5, 8] -> [1, 2, 4, 5, 8]; Array is Sorted.

--------------------
Time Complexity:
--------------------
The bubble sort method of sorting an array of size n requires (n-1) passes and (n-1) comparisons 
on each pass. Thus the total number of comparisons is (n-1) * (n-1) = n^2 - 2n + 1, which is O(n^2). 
Therefore bubble sort is very inefficient when there are more elements to sorting.
"""


# Bubble Sort in Python.
def bubblesort(array, size):
    for i in range(size):
        for j in range(size - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


if __name__ == "__main__":
    array = []
    size = int(input("Enter the number of elements: "))
    for i in range(size):
        ele = int(input("Enter the elements: "))
        array.append(ele)
    print("Original List is ", array)
    bubblesort(array, size)
    print("Sorted List is ", array)


"""
-----------------------------------
Optimized Bubble Sort Algorithm:
-----------------------------------
In bubble sort algorithm, all the comparisons are made even if the array is already sorted. This increases the execution time.

To solve this, we can introduce an extra variable `swapped`. The value of `swapped` is set to True if there 
occurs a swapping of elements. Otherwise, it is set to False. After an iteration, if there is no swapping, 
the value of `swapped` will be False. This means elements are already sorted, and there is no need to perform 
further iterations. This will reduce the execution time and helps to optimize the bubble sort.
"""


# Optimized Bubble Sort in Python.
def OptimizebubbleSort(array):
    for i in range(len(array)):
        # Keep track of Swapping.
        swapped = False
        for j in range(0, len(array) - i - 1):
            # Compare two adjacent elements.
            if array[j] > array[j + 1]:
                # Swapping occurs if elements are not in the intended order.
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

                swapped = True

        if not swapped:
            break


if __name__ == "__main__":
    array = []
    size = int(input("Enter the number of elements: "))
    for i in range(size):
        ele = int(input("Enter the elements: "))
        array.append(ele)
    print("Original List is ", array)
    OptimizebubbleSort(array)
    print("Optimized Sorted List is ", array)
