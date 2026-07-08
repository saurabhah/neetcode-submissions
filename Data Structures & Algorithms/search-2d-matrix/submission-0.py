class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            for col in matrix:
                if target in row or target in col:
                    return True

        
        return False