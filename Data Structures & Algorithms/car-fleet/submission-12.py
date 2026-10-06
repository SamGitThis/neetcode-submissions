class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_s = []

        for i in range(len(speed)):
            p_s.append([position[i], speed[i]])

        p_s = sorted(p_s, key = lambda x: x[0])[::-1]

        fleet = len(position)
        prev = 0

        for p, s in p_s:
            if prev != 0 and (target - p) / s <= prev:
                fleet -= 1
            
            else:
                prev = (target - p) / s

        return fleet