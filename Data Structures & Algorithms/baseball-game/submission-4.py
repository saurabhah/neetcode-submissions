class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ch in operations:
            print(stack)
            if ch == "+":
                
                stack.append(str(int(stack[-1]) + int(stack[-2])))
            elif ch == "C":
                stack.pop()
            elif ch == "D":
                double_r = int(stack[-1])* 2
                stack.append(str(double_r))
            else:
                stack.append(ch)
        print(stack,"final")
        return sum([int(i) for i in stack])