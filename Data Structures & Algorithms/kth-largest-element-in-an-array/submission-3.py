import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)

        lw = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        up = [x for x in nums if x > pivot]

        l, m, u = len(lw), len(mid), len(up)

        if k <= u:
            return self.findKthLargest(up, k)
        elif k > u + m:
            return self.findKthLargest(lw, k - u - m)
        else:
            return mid[0]