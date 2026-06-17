class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        num = sorted(nums)
        ans = []
        length = 1
        
        for i in range(len(nums)):
            if i == len(nums) - 1:
                ans.append(length)
                break
            
            elif num[i] == num[i+1]:
                continue
            
            elif num[i]+1 == num[i+1]:
                length += 1
                
            else:
                ans.append(length)
                length = 1
        
        return max(ans)