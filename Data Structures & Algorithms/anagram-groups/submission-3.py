class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d1 = defaultdict(list)
        
        for s in strs:
            t = tuple(sorted(s))
            d1[t].append(s)
            
        return d1.values()