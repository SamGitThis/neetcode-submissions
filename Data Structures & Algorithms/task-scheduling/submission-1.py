import heapq
import queue

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
            count = {}
            for task in tasks:
                if task not in count:
                    count[task] = 1
                else:
                    count[task] += 1
            
            heap = [-ct for ct in count.values()]
            heapq.heapify(heap)

            q = deque()
            time = 0
            
            while heap or q:
                time += 1

                if not heap:
                    time = q[0][1]

                else:
                    occ = 1 + heapq.heappop(heap)
                    if occ != 0:
                        q.append([occ, n + time])

                if q and time == q[0][1]:
                    heapq.heappush(heap, q.popleft()[0])

            return time





