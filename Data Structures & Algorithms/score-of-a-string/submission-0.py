class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        prev_num  = 0
        for i in range(len(s)-1):
            prev_num = s[i]
            print(ord(s[i]))
            score += abs(ord(s[i]) - ord(s[i+1]))
        
        return score
        