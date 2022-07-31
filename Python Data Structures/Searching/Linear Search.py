"""
Searching is used to find the location where an element is available. There are two types of search techniques.

1.  Linear or Sequential Search
2.  Binary Search

--------------------
Linear Search
--------------------
The time complexity of the Linear Search is O(n) and space complexity is O(1).

Linear Search is the simplest of all searching techniques. In this technique, an ordered or unordered list 
will be searched one by one from the beginning until the desired element is found. If the desired element 
is found in the list, then the search is successful otherwise unsuccessful.

Suppose there are "N" elements organized sequentially on a list. The number of comparisons required to retrieve 
an element from the list purely depends on where the element is stored in the list. If it is the first element, 
one comparison will do; if it is the second element, two comparisons are necessary, and so on. On average, we 
need [(N+1)/2] comparisons to search an element. If the search is not successful, we would need "N" comparisons.
"""


def linearSearch(mylist, key):
    flag = 0
    for i in range(len(mylist)):
        if key == mylist[i]:
            flag = 1
            break
    if flag == 1:
        print("Searched Item found at location ", (i + 1))
    else:
        print("Searched Item Not Found.")


array = [1, 3, 9, 27, 81, 243]
linearSearch(array, key=81)


def recursiveLSearch(mylist, key, index):
    if index < len(mylist):
        if mylist[index] == key:
            print("Searched Item found at location ", (index + 1))
        else:
            recursiveLSearch(mylist, key, index + 1)
    else:
        print("Searched Item Not Found.")


array = [1, 3, 9, 27, 81, 243]
recursiveLSearch(array, key=27, index=0)
