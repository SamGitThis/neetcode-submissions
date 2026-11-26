"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        
        clone = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current = queue.popleft()

            for nei in current.neighbors:
                if nei not in clone:
                    clone[nei] = Node(nei.val)
                    queue.append(nei)

                clone[current].neighbors.append(clone[nei])

        return clone[node]