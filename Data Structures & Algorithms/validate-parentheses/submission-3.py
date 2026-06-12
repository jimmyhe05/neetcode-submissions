class Solution:
    def isValid(self, s: str) -> bool:        
        stack = []

        close_to_open = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if c in close_to_open:
                if not stack or stack[-1] != close_to_open[c]:
                    return False

                stack.pop()

            else:
                stack.append(c)

        return len(stack) == 0
