""" Counting Sort Tutorials: https://www.programiz.com/dsa/counting-sort """

"""
Counting Sort is a sorting algorithm that sorts the elements of an array by counting the number of 
occurrences of each unique element in the array. The count is stored in an auxiliary array and the 
sorting is done by mapping the count as an index of the auxiliary array.

--------------------------------
Working of Counting Sort:
--------------------------------
Step 1: Find out the maximum element `max` from the given array.

Step 2: Initialize an array of length `max+1` with all elements 0.
        This array is used for storing the count of the elements in the array.

Step 3: Store the count of each element at their respective index in the `count` array.

Step 4: Store cumulative sum of the elements of the count array.
        It helps in placing the elements into the correct index of the sorted array.

Step 5: Find the index of each element of the original array in the count array.
        It gives the cumulative count. Place the element at the index calculated as shown in the figure below.

Step 6: After placing each element at its correct position, decrease its count by one.

-------------------------
Complexity Analysis:
-------------------------
Counting Sort has O(n+k) time complexities for all the cases (best case, average case, and worst case).
        Time Complexity:    O(n+k)
        Space Complexity:   O(max)
"""


# Counting Sort in Python.
def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize the count array.
    count = [0] * 10

    # Store the count of each element in the count array.
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cumulative count.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in the count array
    # and place the elements in the output array.
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into the original array.
    for i in range(0, size):
        array[i] = output[i]


if __name__ == "__main__":
    array = []
    size = int(input("Enter the number of elements: "))
    for i in range(size):
        ele = int(input("Enter the elements: "))
        array.append(ele)
    print("Original List is ", array)
    countingSort(array)
    print("Sorted List is ", array)
