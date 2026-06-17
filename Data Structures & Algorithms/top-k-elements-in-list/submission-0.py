class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        ans = []
        
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        while (k > 0):
            m = max(freq.values())
            for i in freq:
                if freq[i] == m:
                    ans.append(i)
                    k -= 1
                    freq.pop(i)
                    break
        return ans