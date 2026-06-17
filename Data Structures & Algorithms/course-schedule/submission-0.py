class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        p = prerequisites
        unvis = 1
        visg = 2
        visd = 3

        g = defaultdict(list)
        for i, j in p:
            g[i].append(j)

        pro = [1] * numCourses

        def dfs(node):
            if pro[node] == 2:
                return False

            if pro[node] == 3:
                return True

            pro[node] = 2
            for nei in g[node]:
                if dfs(nei) is False:
                    return False
            
            pro[node] = 3
            return True

        for i in range(numCourses):
            if dfs(i) is False:
                return False

        return True