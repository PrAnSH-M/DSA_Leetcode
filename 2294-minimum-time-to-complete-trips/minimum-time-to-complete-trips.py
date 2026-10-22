class Solution:

    def canCompleteTotalTrip(self, time: list[int], m: int, totalTrips: int) -> bool:

        n = len(time)

        tripComplete = 0

        for n in time:
            tripComplete += m//n


        return tripComplete >= totalTrips


    def minimumTime(self, time: list[int], totalTrips: int) -> int:

        n = len(time)

        l = 1
        r = max(time) * totalTrips

        while l < r:

            m = l + ((r-l)//2)

            if self.canCompleteTotalTrip(time, m, totalTrips):
                r = m
            
            else:
                l = m + 1

        
        return l
        