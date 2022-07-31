"""
-----------------------------------
Evaluation of Postfix Expression:
-----------------------------------

The postfix expression is evaluated easily by the use of a stack. When a number is seen, it is pushed onto the stack; 
when an operator is seen, the operator is applied to the two numbers that are popped from the stack and the result is 
pushed onto the stack. When an expression is given in postfix notation, there is no need to know any precedence rules.

Algorithm:
-----------
Following is the algorithm for evaluation postfix expressions.

1.  Create a Stack to store operands (or values).
2.  Scan the given expression and do the following for every scanned element.
    a) If the element is an operand (number), PUSH it into the Stack.
    b) If the element is an operator, POP out the last two operands from the Stack.
       Evaluate the operator on the two operands and PUSH the result back to the Stack.
3.  When the entire expression is scanned, the number in the Stack is the final answer.

The time complexity of the evaluation algorithm is O(n), where 'n' is the number of characters in the input expression.

There are the following limitations of the above implementation.
1.  It supports only 4 binary operators "+", "*", "-", and "/". 
    It can be extended for more operators by adding more switch cases.
2.  The allowed operands are only single-digit operands. The program can be extended for multiple digits by
    adding a separator-like space between all elements (operators and operands) of the given expression.
"""


class PostfixEvaluate:
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

    # Evaluation of Postfix Expression.
    def evaluatePostfix(self, exp):
        # Iterate over the expression for conversion.
        for i in exp:
            # If the scanned character is an operand (number), PUSH it to the Stack.
            if i.isdigit():
                self.push(i)
            # If the scanned character is an operator, POP two elements from the Stack, and the result is PUSH back to the Stack.
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))
        return int(self.pop())


if __name__ == "__main__":
    exp = "6523+8*+3+*"
    obj = PostfixEvaluate(len(exp))
    print("Postfix Evaluation: %d" % (obj.evaluatePostfix(exp)))
