class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        w = [0] * 28

        for word in strs:
            for letter in word:
                w[ord(letter) - 96] += 1

            ans[tuple(w)].append(word)
            w = [0] * 28

        return list(ans.values())