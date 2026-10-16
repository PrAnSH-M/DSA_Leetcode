class Solution:

    def quick_sort(self, arr:list) -> list:
        if len(arr) <= 1:
            return arr

        P = arr[-1]

        L = [x for x in arr[:-1] if x[0] < P[0]]
        R = [x for x in arr[:-1] if x[0] >= P[0]]

        L = self.quick_sort(L)
        R = self.quick_sort(R)

        return L + [P] + R


    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        """
            what i am thinking is sorting intervalls with start time 

            intervals = [[1,3],[2,6],[8,10],[15,18]]
            after sort -> [[1,3],[2,6],[8,10],[15,18]]

            then will compare and if over-lapping we will print those two as with starting time of 
            first time list and end time with second list

            if end time of first interval is > then starting time of second time interval

            as in this example
            [1,3] and [2,6]
             so final output will be [[1,6],[8,10],[15,18]]

        """

        final_list = []

        sorted_list = self.quick_sort(intervals)

        for start_time, end_time in sorted_list:
            maxx = 0
            if not final_list:
                final_list.append([start_time, end_time])
            
            # If overlapping
            elif final_list[-1][1] >= start_time:
                final_list[-1][1] = max(final_list[-1][1], end_time)

            # If not overlapping
            else:
                final_list.append([start_time, end_time])

        return final_list


        