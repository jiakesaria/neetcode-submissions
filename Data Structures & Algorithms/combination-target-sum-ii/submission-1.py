class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtracking(index, path, total):
            #base case 
            if total == target:
                res.append(path[:])
                return 
            if index == len(candidates) or total > target:
                return 
            path.append(candidates[index])
            backtracking(index+1, path, total + candidates[index])
            path.pop()
        
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            backtracking(index + 1, path, total)

        backtracking(0, [], 0)
        return res 