"""
Find if an expression has duplicate parenthesis or not.

https://www.geeksforgeeks.org/find-expression-duplicate-parenthesis-not/

--------------
Algorithm:
--------------

1.  Initialize a Stack.
2.  Iterate through the given expression and for each character in the expression:
    a) If the character is an open parenthesis '(', or any of the operators or operands; PUSH it into the top of the Stack.
    b) If the character is close parenthesis ')', then, POP all the characters from the Stack until the matching open parenthesis "(" is found.
    c) Use a counter whose value gets incremented for every character encountered till the opening parenthesis '(' is found.
    d) If the number of characters encountered between the opening and closing parenthesis pair is less than 1, then a pair of duplicate parenthesis 
       is found. Otherwise, there is no occurrence of redundant parenthesis pairs.
    
Below expressions have duplicate parenthesis.

1.  ((a+b)+((c+d))) - The subexpression "c+d" is surrounded by two pairs of brackets.
2.  (((a+(b)))+(c+d)) - The subexpression "a+(b)" is surrounded by two pairs of brackets.

Time Complexity is O(n).
Space Complexity is O(n).
"""

# Function to find duplicate parenthesis in a balanced expression.
def findDuplicateparenthesis(string):
    # Create a Stack of Characters.
    Stack = []
    # Iterate through the given expression.
    for ch in string:
        # If the current character is close parenthesis ")".
        if ch == ")":
            # POP character from the Stack.
            top = Stack.pop()
            # Stores the number of characters between closing and opening parenthesis.
            # If this count is less than 1, then the brackets are redundant.
            elementsInside = 0
            while top != "(":
                elementsInside += 1
                top = Stack.pop()
            if elementsInside < 1:
                return True
        # Push open parenthesis '(', operators and operands into the Stack.
        else:
            Stack.append(ch)
    return False


# Main Code.
if __name__ == "__main__":
    string = "((a+b)+((c+d)))"
    if findDuplicateparenthesis(string) == True:
        print("Duplicate Parenthesis Found.")
    else:
        print("Duplicate Parenthesis Not Found.")
