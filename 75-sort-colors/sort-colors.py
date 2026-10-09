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
        mp = {}

        for i in nums:
            mp[i] = mp.get(i, 0)+1

        print(mp)

        idx = 0

        for key in range(3):
            for i in range(mp.get(key, 0)):
                nums[idx] = key
                idx += 1


            




        