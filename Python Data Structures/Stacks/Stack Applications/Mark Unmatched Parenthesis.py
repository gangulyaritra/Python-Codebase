"""
Identify and mark unmatched parenthesis in an expression.

https://www.geeksforgeeks.org/identify-mark-unmatched-parenthesis-expression/

1.  Input : ((a)    Output : -10a1
2.  Input : (a))    Output : 0a1-1

---------------
Algorithm
---------------

1.  Initialize the Stack.
2.  Run a loop from the start of the string till the end, and for every '(', PUSH it into a Stack.
    a) If the Stack is empty, and we encounter a closing bracket ')', Replace -1 at that index of the string.
    b) Else, replace all opening brackets '(' with 0 and closing brackets ')' with 1. Then POP from the Stack.
"""


def identifyParenthesis(string):
    stack = []
    # Run the loop till the end of the string.
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(string[i])
        elif string[i] == ")":
            if len(stack) == 0:
                string = string.replace(string[i], "-1", 1)
            else:
                # Replace all opening brackets with 0 and closing brackets with 1.
                string = string.replace(string[i], "1", 1)
                string = string.replace(stack[-1], "0", 1)
                stack.pop()
    # If the Stack is not empty then POP out all elements from it and replace -1 at that index of the string.
    while len(stack) != 0:
        string = string.replace(stack[-1], "0", 1)
        stack.pop()

    # Print Final String.
    print(string)


# Main Code.
if __name__ == "__main__":
    str = "(((abc))((d)))))"
    identifyParenthesis(str)
