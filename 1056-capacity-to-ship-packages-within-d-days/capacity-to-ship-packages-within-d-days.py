class Solution:

    def daysTaken(self, weights: list[int], capacity: int) -> int:

        days = 1
        load = 0

        for i in range(len(weights)):
            if load + weights[i] > capacity:
                days += 1
                load = weights[i]
            
            else:
                load += weights[i]

        return days


    def shipWithinDays(self, weights: list[int], days: int) -> int:
        n = len(weights)
        sum = 0
        for n in weights:
            sum += n
        
        l = max(weights)
        r = sum

        while l <= r:
            m = l + ((r-l)//2)

            no_of_days = self.daysTaken(weights, m)

            if no_of_days <= days:
                r = m - 1
            
            else:
                l = m + 1

        return l
                
        