class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ps = [(position[i], speed[i]) for i in range(len(speed))]
        ps = sorted(ps, key = lambda x: x[0])[::-1]

        cur_spe = -1
        fleet = 0
        cur_tm = 0

        for p, s in (ps):
            fleet += 1

            if cur_spe != -1 and (target - p) / s <= cur_tm:
                fleet -= 1
                cur_spe = min(cur_spe, s)
            
            else:
                cur_spe = s
                cur_tm = (target - p) / s

        return fleet