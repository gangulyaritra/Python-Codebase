"""
Searching is used to find the location where an element is available. There are two types of search techniques.

1.  Linear or Sequential Search
2.  Binary Search

-------------------------------
Binary Search. "https://en.wikipedia.org/wiki/Binary_search_algorithm"
-------------------------------
Binary Search searches a sorted array by repeatedly dividing the search interval into half. It begins with an interval covering 
the whole list. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the 
lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.
We have "N" records that have been ordered by keys so that X1 < X2 < ... < XN. When an element "X" is provided, a binary search 
is used to find the corresponding element from the list. In case "X" is present, the search gets successful, otherwise unsuccessful.
In Binary Search, we jump into the middle of the list, where we find array[mid], and compare the search element "X" with array[mid]. 
If X = array[mid], then the desired record has been found. If X < array[mid], then "X" must be in that portion of the list that precedes 
array[mid]. Similarly, if array[mid] > X, then a further search is only necessary for that part of the list, which follows array[mid]. 
If we use a recursive procedure of finding the middle key array[mid] of the un-searched portion of a list, then every unsuccessful 
comparison of the searched element "X" with array[mid] will eliminate roughly half the un-searched portion from consideration.

-------------------------------
Divide and Conquer Algorithm.
-------------------------------
A divide and conquer algorithm is a strategy for solving a large problem by
    1.  Breaking the problem into smaller sub-problems.
    2.  Solving the sub-problems, and
    3.  Combine them to get the desired output.
To use the divide and conquer algorithm, recursion is used.

-------------------------------
How Divide and Conquer Work?
-------------------------------
Here are the steps involved:
    1.  Divide: Divide the given problem into sub-problems using recursion.
    2.  Conquer: Solve the smaller sub-problems recursively. If the subproblem is small enough, then solve it directly.
    3.  Combine: Combine the solutions of the sub-problems that are part of the recursive process to solve the actual problem.

-------------------------------
Binary Search Algorithm.
-------------------------------
1.  Compare the searched element "X" with the middle element of the list.
2.  If the searched element "X" matches with the middle element, we return the middle index of the list.
3.  If the searched element "X" is greater than the middle element, then "X" can only lie in the right 
    half subarray after the middle element. So we recur for the right half.
4.  If the searched element "X" is lesser than the middle element, then "X" can only lie in the left 
    half subarray before the middle element. So we recur for the left half.

-------------------------------
Time Complexity:
-------------------------------
The time complexity of the Binary Search in a successful search is O(log n), and for an unsuccessful search is O(log n).
The space complexity of the Binary Search is O(1).
"""


def BinarySearch(mylist, key):
    mylist.sort()
    low = 0
    high = len(mylist)
    flag = 0
    """
    LOW and HIGH are integer variables such that each time through the loop, either the searched element "X" is found,
    or the "LOW" variable is increased by at least one, or the "HIGH" variable is decreased by at least one. Thus we 
    have two sequences of integers approaching each other and eventually, the "LOW" variable will become greater than 
    the "HIGH" variable causing termination in a finite number of steps if the searched element "X" is not present.
    """
    while low <= high:
        mid = int((low + high) / 2)
        if mylist[mid] == key:
            flag = 1
            break
        else:
            if key < mylist[mid]:
                high = mid - 1
            else:
                low = mid + 1
    if flag == 1:
        print("Searched Item found at the location ", mid + 1)
    else:
        print("Searched Item Not Found.")


array = [5, 4, 8, 3, 8, 0, 1, 4, 7, 23, 56, 19]
BinarySearch(array, 8)


def recursiveBSearch(mylist, key, low, high):
    if low <= high:
        mid = int((low + high) / 2)
        if mylist[mid] == key:
            print("Searched Item found at the location ", mid + 1)
        else:
            if key < mylist[mid]:
                recursiveBSearch(mylist, key, low, mid - 1)
            else:
                recursiveBSearch(mylist, key, mid + 1, high)
    else:
        print("Searched Item Not Found.")


array = [5, 4, 8, 3, 8, 0, 1, 4, 7, 23, 56, 19]
array.sort()
recursiveBSearch(array, key=23, low=0, high=len(array))
