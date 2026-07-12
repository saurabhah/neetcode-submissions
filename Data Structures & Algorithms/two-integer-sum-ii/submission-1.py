class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        from collections import defaultdict
        name_dic = defaultdict(int)

        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if name_dic[tmp]:
                return [name_dic[tmp],i + 1]
            name_dic[numbers[i]] = i + 1
        
        return []
        