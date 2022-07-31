"""
-----------------------------------------------------------
Check for Balanced Brackets in an expression using Stack.
-----------------------------------------------------------

"https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/"

1.  Time Complexity: O(n)
2.  Auxiliary Space: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Traverse the expression string.
        for i in s:
            # If the current character is a starting bracket ('(', or '{', or '['), then PUSH it to the Stack.
            if i in ["(", "{", "["]:
                stack.append(i)
            else:
                if not stack:
                    return False
                # If the current character is a closing bracket (')' or '}' or ']'), then POP the element from the Stack.
                # If the popped character is the matching starting bracket, then fine, otherwise the brackets are not balanced.
                current_char = stack.pop()
                if current_char == "(":
                    if i != ")":
                        return False
                if current_char == "{":
                    if i != "}":
                        return False
                if current_char == "[":
                    if i != "]":
                        return False
        # After complete traversal, if there is some starting bracket left in the Stack then the brackets are not balanced.
        if stack:
            return False
        return True


if __name__ == "__main__":
    expr = "[()]{}{[()()]()}"
    st = Solution()
    if st.isValid(expr) == True:
        print("Balanced")
    else:
        print("Not Balanced")
