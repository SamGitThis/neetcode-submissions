class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rep = set()
        for num in nums:
            if num not in rep:
                rep.add(num)
            else:
                return True

        return False