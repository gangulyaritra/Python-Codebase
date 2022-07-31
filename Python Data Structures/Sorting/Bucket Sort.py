""" Bucket Sort Tutorials: https://www.programiz.com/dsa/bucket-sort """

"""
Bucket Sort is a sorting algorithm that divides the unsorted array elements into several groups called buckets.
Each bucket is then sorted by using any suitable sorting algorithms or recursively applying the same bucket algorithm.
Finally, the sorted buckets are combined to form a final sorted array.

-------------------------
Complexity Analysis:
-------------------------
Bucket Sort has different time complexities for all the cases.
        Best Case Complexity:       O(n+k)
        Average Case Complexity:    O(n)
        Worst Case Complexity:      O(n^2)
        
        Space Complexity:           O(n+k)
"""


# Bucket Sort in Python.
def bucketSort(array):
    bucket = []
    # Create empty buckets.
    for i in range(len(array)):
        bucket.append([])
    # Insert elements into their respective buckets.
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    # Sort the elements of each bucket.
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    # Get the sorted elements.
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


if __name__ == "__main__":
    array = []
    size = int(input("Enter the number of elements: "))
    for i in range(size):
        ele = float(input("Enter the elements: "))
        array.append(ele)
    print("Original List is ", array)
    bucketSort(array)
    print("Sorted List is ", array)
