class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:

        n = len(nums)

        for i in range(n):
            if nums[i] % 2 != 0:

                for j in range(i+1, n):
                    if nums[j] % 2 == 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                        

        return nums