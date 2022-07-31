"""
------------------------------
Reverse a String using Stack
------------------------------

"https://www.geeksforgeeks.org/stack-set-3-reverse-string-using-stack/"

1.  Time Complexity: O(n) where n is the number of characters in the Stack.
2.  Auxiliary Space: O(n) for the Stack.
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

    def revString(self, string):
        n = len(string)
        if string == "":
            print("String is Empty.")
        else:
            # One by one, PUSH all characters of the string to Stack.
            for i in string:
                self.push(i)
            string = ""
            # One by one, POP all characters from the Stack and put them back to the empty string.
            for i in range(0, n):
                string += self.pop()
        return string


if __name__ == "__main__":
    string = "ARITRAGANGULY"
    st = Stack(len(string))
    reverse = st.revString(string)
    print(reverse)
