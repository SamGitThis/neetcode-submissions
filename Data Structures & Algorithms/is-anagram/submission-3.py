class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s1 = defaultdict(list)
        s2 = defaultdict(list)

        for i in range(len(s)):
            if s[i] not in s1:
                s1[s[i]] = 1

            else:
                s1[s[i]] += 1

            if t[i] not in s2:
                s2[t[i]] = 1

            else:
                s2[t[i]] += 1
        print(s1, s2)
        return s1 == s2