class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        n = len(nums)
        num1 = float("Inf")
        num2 = float("Inf")

        for num3 in range(n):
            if nums[num3] <= num1:
                num1 = nums[num3]
            elif nums[num3] <= num2:
                num2 = nums[num3]
            else:
                return True
            
        return False
        