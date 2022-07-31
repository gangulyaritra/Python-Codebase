"""
-----------------------------------
Evaluation of Prefix Expression:
-----------------------------------

Algorithm:
-----------
Following is the algorithm for evaluation prefix expressions.

Step 1: Put a pointer P at the end of the expression.
Step 2: If the character at P is an operand, PUSH it to Stack.
Step 3: If the character at P is an operator, POP two elements from the Stack.
        Operate on these elements according to the operator, and PUSH the result back to the Stack.
Step 4: Decrement P by 1, and go to Step 2 as long as there are characters left to be scanned in the expression.
Step 5: Return the final result that is stored at the top of the Stack.
Step 6: End.
"""


class PrefixEvaluate:
    # Constructor to initialize the class variables.
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.stack = []

    # Check if the Stack is empty.
    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the Stack.
    def peek(self):
        return self.stack[-1]

    # Pop the element from the Stack.
    def pop(self):
        if self.isEmpty() == False:
            self.top -= 1
            return self.stack.pop()
        else:
            print("Stack Underflow.")

    # Push the element to the Stack.
    def push(self, item):
        self.top += 1
        self.stack.append(item)

    # Evaluation of Prefix Expression.
    def evaluatePrefix(self, exp):
        # Iterate over the reverse expression for conversion.
        for i in exp[::-1]:
            # If the scanned character is an operand (number), PUSH it to the Stack.
            if i.isdigit():
                self.push(int(i))
            # If the scanned character is an operator, POP two elements from the Stack, and the result is PUSH back to the Stack.
            else:
                o1 = self.pop()
                o2 = self.pop()
                if i == "+":
                    self.push(o1 + o2)
                elif i == "-":
                    self.push(o1 - o2)
                elif i == "*":
                    self.push(o1 * o2)
                elif i == "/":
                    self.push(o1 / o2)
        return int(self.pop())


if __name__ == "__main__":
    exp = "+9*26"
    obj = PrefixEvaluate(len(exp))
    print("Postfix Evaluation: %d" % (obj.evaluatePrefix(exp)))
