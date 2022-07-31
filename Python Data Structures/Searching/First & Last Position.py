""" Find First and Last Position of Element in Sorted Array. 
    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ """

"""
Given an array of integers `nums` sorted in non-decreasing order. Find the starting and ending position of a given `target` value.

If the target is not found in the array, return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.

------------
Example 1:
------------
Input: nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]

------------
Example 2:
------------
Input: nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]

------------
Example 3:
------------
Input: nums = [], target = 0
Output: [-1, -1]

------------
Example 4:
------------
Input: nums = [1, 3, 5, 5, 5, 5, 67, 123, 125], target = 5
Output: [2, 5], i.e., First Occurrence = 2 & Last Occurrence = 5

------------
Example 5:
------------
Input: nums = [1, 3, 5, 5, 5, 5, 67, 123, 125], target = 67
Output: [6, 6], i.e., First Occurrence = 6 & Last Occurrence = 6
"""

"""
The Naive Approach is to run a for() loop and check the given elements in an array.
    1. Run a for() loop in range i = 0 to n-1.
    2. Assign variables first = -1 and last = -1.
    3. When we find the searched element the first time, update first = i.
    4. Update last = i, whenever we find that element in the list.
    5. We finally print the first and last counters.

    Time Complexity: O(n)
    Auxiliary Space: O(1)
"""

# Function for finding the first and last occurrence of an element.
def findFirstAndLast(array, target):
    first = -1
    last = -1
    for i in range(0, len(array)):
        if target != array[i]:
            continue
        if first == -1:
            first = i
        last = i

    if first != -1:
        print([first, last])
    else:
        print([-1, -1])


if __name__ == "__main__":
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    target = 8
    findFirstAndLast(arr, target)


""" 
An efficient solution to this problem is to use a Binary Search. 

    Time Complexity: O(log n)
    Auxiliary Space: O(1)
"""

# For the first occurrence of a number.
def firstOccur(array, target):
    LOW = 0
    HIGH = len(array) - 1
    res = -1
    while LOW <= HIGH:
        mid = (LOW + HIGH) // 2
        if array[mid] > target:
            HIGH = mid - 1
        elif array[mid] < target:
            LOW = mid + 1
        else:
            res = mid
            HIGH = mid - 1
    return res


# For the last occurrence of a number.
def lastOccur(array, target):
    LOW = 0
    HIGH = len(array) - 1
    res = -1
    while LOW <= HIGH:
        mid = (LOW + HIGH) // 2
        if array[mid] > target:
            HIGH = mid - 1
        elif array[mid] < target:
            LOW = mid + 1
        else:
            res = mid
            LOW = mid + 1
    return res


if __name__ == "__main__":
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    target = 2
    print([firstOccur(arr, target), lastOccur(arr, target)])
