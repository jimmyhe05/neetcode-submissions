class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), reverse=True)
        slowest_t = 0
        fleet = 0

        for p, s in pair:
            t = (target - p) / s
            
            if t > slowest_t:
                fleet += 1
                slowest_t = t

        return fleet


                