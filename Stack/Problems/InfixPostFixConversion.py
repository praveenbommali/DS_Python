# Converting the Infix expression into postfix expression as follows

class InfixPostFixConvImpl(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.output = []
        self.operandStack = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '%': 2, '^': 3}

    def isOperand(self, element):
        return element.isalpha()

    def push(self, element):
        self.top += 1
        self.operandStack[self.top] = element

    def pop(self):
        element = self.operandStack[self.top]
        self.top -= 1
        return element

    def peek(self):
        return self.operandStack[self.top]

    def isPrecedence(self, element):

        try:
            op1 = self.precedence[element]
            op2 = self.precedence[self.peek()]
            return True if op1 <= op2 else False
        except KeyError:
            return False

    def isEmpty(self):
        return self.top != -1

    def infix_postfix_conv(self, expression):

        # Iterating over the expression characters
        for i in expression:
            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while (not self.isEmpty()) and self.peek() != '(':
                    self.output.append(self.pop())
                if (not self.isEmpty()) and self.peek() != '(':
                    print("Wrong expression :: paranthesis missing ")
                    return -1
            else:
                while (not self.isEmpty()) and self.isPrecedence(i):
                    self.output.append(self.pop())
                self.push(i)


if __name__ == '__main__':
    exp = "a+b*c"
    infixpostfixConvImpl = InfixPostFixConvImpl(len(exp))
    infixpostfixConvImpl.infix_postfix_conv(exp)
