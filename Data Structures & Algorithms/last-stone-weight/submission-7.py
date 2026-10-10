import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-x for x in stones]

        heapq.heapify(s)

        while len(s) > 1:
            ft = heapq.heappop(s)
            sd = heapq.heappop(s)

            if ft != sd:
                if ft > sd:
                    heapq.heappush(s, -(ft - sd))
                else:
                    heapq.heappush(s, -(sd - ft))

        return -s[0] if s else 0