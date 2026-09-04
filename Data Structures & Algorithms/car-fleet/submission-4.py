class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ps = [(position[i], speed[i]) for i in range(len(speed))]
        ps = sorted(ps, key = lambda x: x[0])[::-1]

        fleet = 0
        prev_tm = 0

        for p, s in (ps):
            fleet += 1

            if prev_tm != 0 and (target - p) / s <= prev_tm:
                fleet -= 1
            
            else:
                prev_tm = (target - p) / s

        return fleet