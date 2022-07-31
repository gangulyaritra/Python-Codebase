""" Search Insert Position of K in a Sorted Array.  https://leetcode.com/problems/search-insert-position/ """

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order. Write an algorithm with O(log n) runtime complexity.

------------
Example 1:
------------
Input: nums = [1, 3, 5, 6], target = 5
Output: 2

------------
Example 2:
------------
Input: nums = [1, 3, 5, 6], target = 2
Output: 1

------------
Example 3:
------------
Input: nums = [1, 3, 5, 6], target = 7
Output: 4


Follow the steps below to solve the problem:
    1. Iterate over every element of the array and search for integer K.
    2. If an array element is found to be equal to K, then print the index of K.
    3. Otherwise, if any array element is found to be greater than K, print that index as the insert position of K.
       If no element is found to be exceeding K, the K element must be inserted after the last array element.

    Time Complexity: O(N)
    Auxiliary Space: O(1)
"""


def searchInsert(array, K):
    for i in range(len(array)):
        if array[i] == K:
            return i
        elif array[i] > K:
            return i
    return len(array)


if __name__ == "__main__":
    array = [1, 3, 5, 6]
    K = 5
    print(searchInsert(array, K))

"""
------------------------
Efficient Approach:
------------------------
To optimize the above approach, the idea is to use Binary Search. Follow the steps below to solve the problem:
    1. Set `LOW` and `HIGH` as 0 and len(array), where the `LOW` and `HIGH` variables denote the lower and upper bound of the search space respectively.
    2. Calculate mid = (LOW + HIGH)/2.
    3. If array[mid] is found to be equal to K, print `mid` as the required answer.
    4. If array[mid] exceeds K, set HIGH = mid - 1. Otherwise, set LOW = mid + 1.

    Time Complexity: O(log N)
    Auxiliary Space: O(1)
"""


def bsearchInsert(array, K):
    LOW = 0
    HIGH = len(array) - 1
    while LOW <= HIGH:
        mid = (LOW + HIGH) // 2
        if array[mid] == K:
            return mid
        elif array[mid] < K:
            LOW = mid + 1
        else:
            HIGH = mid - 1
    return HIGH + 1


if __name__ == "__main__":
    array = [1, 3, 5, 6]
    K = 7
    print(bsearchInsert(array, K))
