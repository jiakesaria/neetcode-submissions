class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #elements of 2d matrix -> a list 
        m = len(matrix) #rows
        n = len(matrix[0]) #cols
        l = 0
        r = (m * n) - 1
        while l <= r:
            mid = l + (r - l)//2
            # m to matrix[i][j]
            i = int(mid // n)
            j = int(mid % n)
            if matrix[i][j] == target:
                return True 
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return False

        