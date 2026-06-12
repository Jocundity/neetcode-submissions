class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers_stack = []
        operators = {"+", "-", "*", "/"}

        for char in tokens:
            if char not in operators:
                numbers_stack.append(int(char))
            else:
                # If operator, pop last two items
                op2 = numbers_stack.pop()
                op1 = numbers_stack.pop()

                # Compute result and push onto stack
                if char == "+":
                    result = op1 + op2
                if char == "-":
                    result = op1 - op2
                if char == "*":
                    result = op1 * op2
                if char == "/":
                    result = int(op1 / op2)

                numbers_stack.append(result)

        return numbers_stack[0]
        