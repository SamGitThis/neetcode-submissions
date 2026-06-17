class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def val_k(k):
            
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
                
            if hours <= h:
                return True
            return False
        
        low, high = 1, max(piles)
        
        while low < high:
            k = (low+high) // 2
            
            if val_k(k):
                high = k
            
            else:
                low = k + 1
                
        return high