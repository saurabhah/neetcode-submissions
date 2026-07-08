class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        print(res)
        return res
        

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            lenght = int(s[i:j])
            word = s[j+1:j+1+lenght]
            res.append(word)

            i = j+1+lenght
        
        return res
