from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = defaultdict(list)

        for i in range(len(nums)):
            index[nums[i]].append(i)


        print(index)
        for num in nums:
            if target - num in index:
                if num == target - num and len(index[num]) > 1:
                    return [ index[num][0], index[num][1]]

                elif num == target - num and len(index[num]) == 1:
                    pass
                
                else:
                    return [index[num][0], index[target - num][0]]