class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        d1 = dict()
        d2 = dict()

        if l1 != l2:
            return False

        for i in range(l1):
            if s[i] not in d1.keys():
                d1[s[i]] = 1
            else:
                d1[s[i]] += 1

            if t[i] not in d2.keys():
                d2[t[i]] = 1
            else:
                d2[t[i]] += 1
        
        return d1 == d2