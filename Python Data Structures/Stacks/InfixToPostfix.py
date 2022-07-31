"""
-----------------------------------
Conversion from Infix to Postfix:
-----------------------------------

The procedure to convert from infix expression to postfix expression is as follows:

1.  Scan the infix expression from left to right.
2.  a) If the scanned symbol is left parenthesis, push it onto the Stack.
    b) If the scanned symbol is an operand, then place it directly in the postfix expression (output).
    c) If the scanned symbol is a right parenthesis, then go on popping all the items from the Stack 
       and place them in the postfix expression till we get the matching left parenthesis.
    d) If the scanned symbol is an operator, then go on removing all the operators from the Stack and 
       place them in the postfix expression, if and only if the precedence of the operator which is on 
       the top of the Stack is greater than (or greater than or equal) to the precedence of the scanned 
       operator and push the scanned operator onto the Stack otherwise, push the scanned operator onto the Stack.
"""


class Conversion:
    # Constructor to initialize the class variables.
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This list is used as a Stack.
        self.array = []
        # This list is used as a Output List.
        self.output = []
        # Precedence Setting.
        self.precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    # Check if Stack is Empty.
    def isEmpty(self):
        return True if self.top == -1 else False

    # Display the last element from the Stack.
    def peek(self):
        return self.array[-1]

    # Pop the element from the Stack.
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            print("Stack Underflow")

    # Push the element to the Stack.
    def push(self, item):
        self.top += 1
        self.array.append(item)

    # Check if the given character is Operand.
    def isOperand(self, ch):
        return ch.isalpha()

    # Check if the precedence of the Operator is strictly less than the top of Stack.
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):
        # Iterate over the expression for Conversion.
        for i in exp:
            # If the character is an operand, add it to output.
            if self.isOperand(i) == True:
                self.output.append(i)
            # If the character is an '(', push it to Stack.
            elif i == "(":
                self.push(i)
            # If the scanned character is an ')', pop and output all elements from the stack until '(' is found.
            elif i == ")":
                while self.isEmpty() == False and self.peek() != "(":
                    a = self.pop()
                    self.output.append(a)
                if self.isEmpty() == False and self.peek() != "(":
                    return -1
                else:
                    self.pop()
            # An Operator is Encountered.
            else:
                while self.isEmpty() == False and self.notGreater(i):
                    self.output.append(self.pop())
                self.push(i)

        # Pop all the Operator from the Stack.
        while self.isEmpty() == False:
            self.output.append(self.pop())
        print("".join(self.output))


if __name__ == "__main__":
    exp = "a+b*c+(d*e+f)*g"
    obj = Conversion(len(exp))
    obj.infixToPostfix(exp)
