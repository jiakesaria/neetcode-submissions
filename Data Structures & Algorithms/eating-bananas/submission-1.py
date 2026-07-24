class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)  
        res = -1     
        while l <= r:
            k = l + (r-l)//2 
            #calc total hrs it takes using that k 
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/k)
            if hrs <= h:
                res = k 
                r = k - 1
                #return k
            elif hrs > h:
                l = k + 1
        return res 


            

        