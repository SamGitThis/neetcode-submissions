class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for strg in strs:
            
            ssort = tuple(sorted(strg))
            res[ssort].append(strg)

        return list(res.values())