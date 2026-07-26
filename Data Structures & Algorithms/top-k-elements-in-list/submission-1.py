class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        
        for num in nums:
            if num not in frequency:
                frequency[num] = 1

            else:
                frequency[num] += 1

        frequency = sorted(frequency.items(), key = lambda x: x[1], reverse = True)
        ans = []

        for i in range(k):
            ans.append(frequency[i][0])

        return ans