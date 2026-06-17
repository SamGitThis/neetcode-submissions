class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        st = [0] * numCourses
        path = []

        for i, j in prerequisites:
            g[i].append(j)
        
        def dfs(node):
            if st[node] == 1:
                return False
            if st[node] == 2:
                return True

            st[node] = 1
            for nei in g[node]:
                if not dfs(nei):
                    return False

            st[node] = 2
            path.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return path