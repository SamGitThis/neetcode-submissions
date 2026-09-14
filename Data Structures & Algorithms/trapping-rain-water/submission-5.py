class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = [], [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                cur_max = 0
                l_max.append(0)

            else:
                cur_max = max(cur_max, height[i-1])
                l_max.append(cur_max)

        cur_max = 0
        total = 0
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                continue

            else:
                cur_max = max(cur_max, height[i+1])
                r_max[i] = cur_max

            value = max(min(l_max[i], r_max[i]) - height[i], 0)
            total += value

        return total