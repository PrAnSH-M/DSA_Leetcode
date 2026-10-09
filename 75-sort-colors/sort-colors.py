class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # approach 1
        """
            in approach one we doing is counting the count of 0,1,2 and then again iterating over array and
            putting value back but first 0 then 1 and at last 2
        """
        # mp = {}

        # for i in nums:
        #     mp[i] = mp.get(i, 0)+1

        # # print(mp)

        # idx = 0

        # for key in range(3):
        #     # print(key)
        #     for i in range(mp.get(key, 0)):
        #         nums[idx] = key
        #         idx += 1

        """
            approach 2 using 3 pointer i, j and k where i for 0, j for 1 and k for 3
            when j crosses the k means our array is complete and we will exit the loop

        """
        n = len(nums)

        i = 0
        j = 0
        k = n - 1

        while j <= k:
            # if nums[j] = 0 swap with nums[i] and i++
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j+=1
            
            # if nums[j] == 2 swap with k and k--
            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
            
            else:
                j += 1

        


            




        