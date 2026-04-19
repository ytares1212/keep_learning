# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:

# Input: s = "1 + 1"
# Output: 2

# Example 2:

# Input: s = " 2-1 + 2 "
# Output: 3

# Example 3:

# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        current_result = 0
        sign = 1  # 1 means positive, -1 means negative

        for char in s:
            if char.isdigit():
              # why *10 here? because we are building the current number from its digits. 
              # For example, if we have '1' followed by '2', we want to form the number 12. So when we see '1', current_number becomes 1. 
              # When we see '2', we need to multiply the existing current_number (which is 1) by 10 and then add the new digit (2) to get 12.
                current_number = current_number * 10 + int(char)
            elif char in ['+', '-']:
                current_result += sign * current_number
                current_number = 0
                sign = 1 if char == '+' else -1
            elif char == '(':
                stack.append(current_result)
                stack.append(sign)
                current_result = 0
                sign = 1
            elif char == ')':
                current_result += sign * current_number
                current_number = 0
                current_result *= stack.pop()  # pop the sign
                current_result += stack.pop()   # pop the result before the parenthesis

        return current_result + (sign * current_number)