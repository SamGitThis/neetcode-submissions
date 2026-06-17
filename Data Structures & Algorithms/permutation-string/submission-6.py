class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        perm = {}
        ln = len(s1)
        
        for i in s1:
            if i in perm:
                perm[i] += 1
            else:
                perm[i] = 1
        
        counter = {}
        
        for i in range(ln):
            if s2[i] not in counter:
                counter[s2[i]] = 1
            else:
                counter[s2[i]] += 1
                
        if counter == perm:
            return True
        
        l = 0
        for r in range(i+1, len(s2)):
            
            if s2[r] in counter:
                counter[s2[r]] += 1
            else:
                counter[s2[r]] = 1
            
            counter[s2[l]] -= 1
            
            if counter[s2[l]] == 0:
                del counter[s2[l]]
            l += 1
            if counter == perm:
                return True
            

        return False