""" Selection Sort Tutorials: https://www.programiz.com/dsa/selection-sort """

"""
Selection Sort is a sorting algorithm that selects the smallest element from an unsorted list 
in each iteration and places that element at the beginning of the unsorted list.


Selection Sort will require no more than (n-1) interchanges. Suppose X is an array of size N stored in memory. 
The selection sort algorithm first selects the smallest element in the array X and places it at array position 0; 
then it selects the next smallest element in the array X and places it at array position 1. It simply continues 
this procedure until it places the largest element in the last position of the array.

The array is passed through (n-1) times, and the smallest element is placed in its respective position in the 
array as detailed below:

Pass 1: Find the location j of the smallest element in the array X[0], X[1], ......., X[n-1], 
        and then interchange X[j] with X[0]. Then X[0] is sorted.

Pass 2: Leave the first element and find the location j of the smallest element in the sub-array 
        X[1], X[2], ......., X[n-1], and then interchange X[1] with X[j]. Then X[0], X[1] are sorted.

Pass 3: Leave the first two elements and find the location j of the smallest element in the sub-array 
        X[2], X[3], ......., X[n-1], and then interchange X[2] with X[j]. Then X[0], X[1], X[2] are sorted.

Pass (n-1): Find the location j of the smaller of the elements X[n-2] and X[n-1], and then interchange 
            X[j] and X[n-2]. Then X[0], X[1], ......., X[n-2] are sorted. During this pass X[n-1] will be 
            the largest element, and so the entire array is sorted.

--------------------
Time Complexity:
--------------------
In general, we prefer selection sort, in the case where the insertion sort or the bubble sort requires exclusive swapping. 
Despite the superiority of the selection sort over bubble sort and the insertion sort (there is a significant decrease in runtime), 
its efficiency is also O(n^2) for n data items.
"""


# Selection Sort in Python.
def selectionSort(X, low, high):
    for i in range(low, high + 1):
        minindex = i
        for j in range(i + 1, high + 1):
            if X[j] < X[minindex]:
                minindex = j
        temp = X[i]
        X[i] = X[minindex]
        X[minindex] = temp


if __name__ == "__main__":
    array = []
    size = int(input("Enter the number of elements: "))
    for i in range(size):
        ele = int(input("Enter the elements: "))
        array.append(ele)
    print("Original List is ", array)
    selectionSort(array, 0, size - 1)
    print("Sorted List is ", array)
