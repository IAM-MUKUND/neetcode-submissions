class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted([[p, s] for p, s in zip(position, speed)], reverse=True)

        maxtime = 0
        fleets = 0
        for p, s in pair:
            time = (target - p) / s
            if time > maxtime:
                maxtime = time
                fleets += 1
        return fleets