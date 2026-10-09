class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:

        """
            first calculate the sumEven 
            second check operation and if the index has a even num means it has contributed in first sum 
            so sumEven - that index val
            third apply the operation 
            fourth if after applying that op if that index val is even then sumEven + after opt val of that index
            at the end return the array of sumEven after each op

            Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
            Output: [8,6,2,4]

        """

        n = len(nums)
        q = len(queries)

        sumEven = 0
         # step 1 -> calculate sumEven
        for i in range(n):
            if nums[i] % 2 == 0:
                sumEven += nums[i]

        res = []
        
        # step 2 check ops
        for i in range(q):
            val = queries[i][0]
            idx = queries[i][1]

            # subtract the old val from sum even if its even
            if nums[idx] % 2 == 0:
                sumEven -= nums[idx]
            
            # apply ops
            nums[idx] += val

            # add the new val to sum even if its even
            if nums[idx] % 2 == 0:
                sumEven += nums[idx]

            res.append(sumEven)
        
        return res

            

        