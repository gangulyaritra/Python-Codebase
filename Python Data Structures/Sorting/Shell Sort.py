""" Shell Sort Tutorials: https://www.programiz.com/dsa/shell-sort """

"""
Shell Sort is a generalized version of the insertion sort algorithm. It first sorts elements that are 
far apart from each other and successively reduces the interval between the elements to be sorted.

The interval between the elements is reduced based on the sequence used.
Some of the optimal sequences that can be used in the shell sort algorithm are:

    1. Shell's Original Sequence: N/2, N/4, ..., 1
    2. Knuth's Increments: 1, 4, 13, ..., (3^k - 1)/2
    3. Hibbard's Increments: 1, 3, 7, 15, 31, 63, 127, 255, 511, ...
    4. Papernov & Stasevich Increments: 1, 3, 5, 9, 17, 33, 65, ...

The performance of the shell sort depends on the type of sequence used for a given input array.

-------------------------
Working of Shell Sort:
-------------------------
Step 1: Suppose we need to sort the following array, i.e., array = [9, 8, 3, 7, 5, 6, 4, 1].

Step 2: We are using the Shell's original sequence, i.e., (N/2, N/4, ..., 1) as intervals in our algorithm.

Step 3: In the first loop, if the array size is N = 8, then the elements lying at the interval of N/2 = 4 
        are compared and swapped if they are not in order.

        a) The 0th element gets compared with the 4th element.
        b) If the 0th element is greater than the 4th element, then the 4th element is first stored in 
           the `temp` variable, and then we move the 0th element to the 4th position. Finally, the element 
           stored in the `temp` variable is moved to the 0th position.
        c) This process goes on for all the remaining elements.

Step 4: In the second loop, the elements lying at the interval of N/4 = 8/4 = 2 are compared and swapped 
        if they are not in order.

        The elements at 4th and 2nd position are compared. The elements at 2nd and 0th position are also 
        compared. All the elements in the array lying at the current interval are compared. The same process 
        goes on for all the remaining elements.

Step 5: Finally, when the interval is N/8 = 8/8 = 1, the array elements lying at the interval of 1 are sorted. 
        The array is now completely sorted.

-------------------------
Complexity Analysis:
-------------------------
Shell Sort is an unstable sorting algorithm because this algorithm does not examine the elements lying in between the intervals.

Time Complexity:
    a)  Best Case:      O(n log n)
    b)  Average Case:   O(n log n)
    c)  Worst Case:     O(n^2)

Space Complexity:   O(1)
"""


# Shell Sort in Python.
def shellSort(array, n):
    # Rearrange elements at each n/2, n/4, n/8, ..., intervals.
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2


if __name__ == "__main__":
    array = []
    size = int(input("Enter the number of elements: "))
    for i in range(size):
        ele = int(input("Enter the elements: "))
        array.append(ele)
    print("Original List is ", array)
    shellSort(array, size)
    print("Sorted List is ", array)
