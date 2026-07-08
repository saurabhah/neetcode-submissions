class Solution:
    def isValid(self, s: str) -> bool:
        sample_dict = {')':'(', '}':'{', ']':'['}

        stack = []

        for c in s:
            if c in sample_dict:
                if stack and stack[-1] == sample_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        