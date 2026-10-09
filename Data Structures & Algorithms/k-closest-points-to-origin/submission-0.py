class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dist = {}
        point_count = {}

        for p1, p2 in points:
            d = math.sqrt(p1*p1 + p2*p2)
            dist[(p1,p2)] = d

            if (p1, p2) in point_count:
                point_count[(p1, p2)] += 1
            else:
                point_count[(p1, p2)] = 1

        dist = sorted(dist.items(), key = lambda item: item[1])
        ans = []
        i = 0

        while k:
            point = dist[i][0]
            
            while point_count[point] != 0:
                ans.append(list(point))
                k -= 1
                point_count[point] -= 1

            i += 1

        return ans