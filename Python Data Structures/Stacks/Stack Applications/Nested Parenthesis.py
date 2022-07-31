"""
-------------------------------------------------
Maximum depth of nested parenthesis in a String.
-------------------------------------------------

"https://www.geeksforgeeks.org/find-maximum-depth-nested-parenthesis-string/"

1.  Time Complexity : O(n)
2.  Auxiliary Space : O(n)
"""


class Stack:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.stack = []

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.stack[-1]

    def push(self, item):
        self.top += 1
        self.stack.append(item)

    def pop(self):
        if self.isEmpty() == False:
            self.top -= 1
            return self.stack.pop()
        else:
            print("Stack Underflow.")

    def maxDepth(self, string):
        max = 0
        count = 0
        # Traverse the String, do the following for every character.
        for i in string:
            # If the current character is "(", PUSH it into the Stack.
            if i in "(":
                self.push(i)
                count += 1
                # Maintain maximum count during the traversal.
                if count > max:
                    max = count
            # If the current character is ")", POP an element from the Stack.
            elif i in ")":
                self.pop()
                count -= 1
        if count != 0:
            print("String Unbalanced.")
        return max


if __name__ == "__main__":
    string = "(a(b)(c)(d(e(f)g)h)I(j(k)l)m)"
    st = Stack(len(string))
    depth = st.maxDepth(string)
    print("Maximum Depth is ", depth)
