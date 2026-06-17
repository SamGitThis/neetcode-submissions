class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for strg in strs:
            count = [0] * 26

            for char in strg:
                count[ord(char) - ord('a')] += 1
            
            res[tuple(count)].append(strg)

        return list(res.values())