""" Merge Sort Tutorials: https://www.programiz.com/dsa/merge-sort """

"""
Merge Sort is one of the most popular sorting algorithms based on the principle of the Divide and Conquer algorithms. 
In Merge Sort, a problem gets divided into multiple sub-problems. Each sub-problem is solved individually. 
Finally, these sub-problems are combined to form the final solution.

The Merge Sort function repeatedly divides the array into two halves until we reach a stage where we try to perform Merge Sort 
on a subarray of size 1. After that, the merge function comes into play and combines the sorted arrays into larger arrays until 
the whole array is merged.

-------------------------------
Working of Merge Sort.
-------------------------------
The merge function works as follows:

1.  Create copies of the subarrays L <- A[p..q] and M <- A[q+1 ... r].
2.  Create three pointers i, j and k.
        a.  i maintains current index of L, starting at 1.
        b.  j maintains current index of M, starting at 1.
        c.  k maintains the current index of A[p..q], starting at p.
3.  Until we reach the end of either L or M, pick the larger among the elements 
    from L and M and place them in the correct position at A[p..q].
4.  When we run out of elements in either L or M, pick up the remaining elements and put in A[p..q].

-------------------------
Complexity Analysis:
-------------------------
Merge Sort has O(n log n) time complexities for all the cases (best case, average case, and worst case).
        Time Complexity:    O(n log n)
        Space Complexity:   O(n)
"""


# Merge Sort in Python.
def mergeSort(array):
    if len(array) > 1:
        # `r` is the point where the array is divided into two subarrays.
        r = len(array) // 2
        L = array[:r]
        M = array[r:]
        # Sort the two halves.
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0
        """
        Until we reach either end of either L or M, pick the larger among elements L and M 
        and place them in the correct position at A[p....r].
        """
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        """
        When we run out of elements in either L or M, pick up the remaining elements and put them in A[p..r].
        """
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Main Function.
if __name__ == "__main__":
    array = []
    size = int(input("Enter the number of elements: "))
    for i in range(size):
        ele = int(input("Enter the elements: "))
        array.append(ele)
    print("Original List is ", array)
    mergeSort(array)
    print("Sorted List is ", array)
