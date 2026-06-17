from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1, l2 = len(s), len(t)
        d1 = defaultdict(list)
        d2 = defaultdict(list)

        if l1 != l2:
            return False

        for i in range(l2):
            if s[i] not in d1:
                d1[s[i]] = 1

            else:
                d1[s[i]] += 1

            if t[i] not in d2:
                d2[t[i]] = 1

            else:
                d2[t[i]] += 1

        return d1 == d2