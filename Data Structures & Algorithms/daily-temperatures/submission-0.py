class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stck = []

        for i, v in enumerate(temperatures):
            while stck and v > stck[-1][0]:
                val, indx = stck.pop()
                result[indx] = i - indx 
            stck.append((v, i))
        
        return result 