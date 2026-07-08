class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        count_word = defaultdict(list)

        for i in strs:
            i_join = "".join(sorted(i))
            count_word[i_join].append(i)
        
        return list(count_word.values())
          
            
        