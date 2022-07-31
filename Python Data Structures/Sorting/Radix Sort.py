""" Radix Sort Tutorials: https://www.programiz.com/dsa/radix-sort """

"""
Radix Sort is a sorting algorithm that sorts the elements by first grouping the individual digits of the same place value. 
Then, this algorithm sort the elements according to their increasing/decreasing order.

Suppose we have an array of 8 elements. First, we will sort the elements based on the value of the unit place. 
Then, we will sort the elements based on the value of the tenth place. This process goes on until the last significant place.

-------------------------
Working of Radix Sort.
-------------------------
Step 1: Find the largest element in the array, i.e., `max`. Let `X` be the number of digits in `max`.
        `X` gets calculated because we have to go through all the significant places of all elements.

        In this array [121, 432, 564, 23, 1, 45, 788], we have the largest number 788.
        It has three digits. Therefore, the loop should go up to a hundred's place (i.e., 3 times).

Step 2: Now, go through each significant place one by one. Use any stable sorting technique 
        to sort the digits at each significant place. We have used counting sort for this. 
        Sort the elements based on the unit place digits (X=0).

Step 3: Now, sort the elements based on digits at tens place (X=10).

Step 4: Finally, sort the elements based on the digits at hundred's place (X=100).

-------------------------
Complexity Analysis:
-------------------------
Radix Sort has O(n+k) time complexities for all the cases (best case, average case, and worst case).
        Time Complexity:    O(n+k)
        Space Complexity:   O(max)

Since Radix Sort is a non-comparative algorithm, it has advantages over comparative sorting algorithms.
For the radix sort that uses counting sort as an intermediate stable sort, the time complexity is O(d(n+k)).
Here, `d` is the number cycle, and O(n+k) is the time complexity of the Counting Sort.

Therefore, Radix Sort has linear time complexity, which is better than O(n log n) of comparative sorting algorithms.

If we take very large digit numbers or the number of other bases like 32-bit and 64-bit numbers, 
then although it can perform in linear time, the intermediate sort takes a large space. This reason 
makes radix sort space inefficient. Hence this sort is not used in software libraries.
"""


# Radix Sort in Python.

# Use counting sort to sort the elements based on significant places.
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    # Calculate the count of elements.
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1
    # Calculate the cumulative count.
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Place the elements in sorted order.
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]


# Function to implement Radix Sort.
def radixSort(array):
    # Get maximum element.
    max_element = max(array)
    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


# Main Function.
if __name__ == "__main__":
    array = []
    size = int(input("Enter the number of elements: "))
    for i in range(size):
        ele = int(input("Enter the elements: "))
        array.append(ele)
    print("Original List is ", array)
    radixSort(array)
    print("Sorted List is ", array)
