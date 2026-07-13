class Solution:

    def encode(self, strs: List[str]) -> str:
        ans =""
        for word in strs:
            ans += str(len(word)) + "#" + word
        return ans

        
    def decode(self, s: str) -> list[str]:
        ans = []
        i = 0
            
        while i < len(s):
            # Find the delimiter '#' starting from index i
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the length of the string and convert it to an integer
            length = int(s[i:j])
            print(length)
            # The word starts right after '#' (at j + 1) and spans 'length' characters
            word = s[j + 1 : j + 1 + length]
            ans.append(word)
            
            # Move the pointer to the start of the next encoded block
            i = j + 1 + length
            
        return ans

        
