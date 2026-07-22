class Solution:
    def isValid(self, s: str) -> bool:
        sample_dict = {')':'(', '}':'{', ']':'['}
        stack = []

        for b in s:
            print(stack)
            if b in sample_dict:
                if stack and stack[-1] == sample_dict[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        print(stack)

        return True if not stack else False


        