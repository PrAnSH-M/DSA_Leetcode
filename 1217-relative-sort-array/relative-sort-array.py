class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:

        # count sort 
        """
        what i am thinking is we make a count arr using nums1 and then increament there count first by nums1 and then by nums2

        after filling count array we will loop of over count arr
        and fill nums1 when all count arr val are 0 we will left with those val which are not in nums2
        we will add those at the end
        """

        n = len(arr1)
        m = len(arr2)

        maxx = max(arr1)

        counts = [0] * (maxx+1)

        final_arr = []

        # for arr1
        for i in arr1:
            counts[i] += 1
        
        # Add elements in arr2 order
        for num in arr2:
            while counts[num] > 0:
                final_arr.append(num)
                counts[num] -= 1
        
        # print(counts)
        for num in range(maxx+1):
            while counts[num] > 0:
                final_arr.append(num)
                counts[num] -=1

        return final_arr
            
        
