""" Quick Sort Tutorials: https://www.programiz.com/dsa/quick-sort """

"""
Quicksort is a sorting algorithm based on the divide and conquer approach where:

1.  An array is divided into subarrays by selecting a pivot element (element selected from the array).

    While dividing the array, the pivot element should be positioned in such a way that elements less 
    than the pivot are kept on the left side, and elements greater than the pivot are on the right side of the pivot.

2.  The left and right subarrays are also divided using the same approach. 
    This process continues until each subarray contains a single element.

3.  At this point, elements are already sorted. Finally, elements are combined to form a sorted array.

-------------------------
Complexity Analysis:
-------------------------

Time Complexity:
    a)  Best Case:      O(n log n)
    b)  Average Case:   O(n log n)
    c)  Worst Case:     O(n^2)

Space Complexity:   O(log n)
"""

""" Quick Sort in Python. """

# Function to find the partition position.
def partition(array, low, high):

    # Choose the rightmost element as the pivot.
    pivot = array[high]

    # Pointer for Greater Element.
    i = low - 1

    # Traverse through all elements and compare each element with pivot.
    for j in range(low, high):
        if array[j] <= pivot:
            # If elements smaller than pivot are found, swap it with the greater element pointed by i.
            i = i + 1

            # Swap element at i with the element at j.
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i.
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where the partition is done.
    return i + 1


# Function to perform Quicksort.
def quickSort(array, low, high):
    if low < high:
        """
        Find pivot elements such that elements smaller than the pivot are on the left and
        elements greater than the pivot are on the right.
        """
        pi = partition(array, low, high)

        # Recursive call on the left of the pivot.
        quickSort(array, low, pi - 1)

        # Recursive call on the right of the pivot.
        quickSort(array, pi + 1, high)


if __name__ == "__main__":
    array = []
    size = int(input("Enter the number of elements: "))
    for i in range(size):
        ele = int(input("Enter the elements: "))
        array.append(ele)
    print("Original List is ", array)
    quickSort(array, 0, size - 1)
    print("Sorted List is ", array)
