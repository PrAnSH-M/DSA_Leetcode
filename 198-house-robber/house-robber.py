class Solution:
    def solve(self, nums: List[int], i: int, dp: List[int]) -> int:
        if i >= len(nums):
            return 0
        if dp[i] != -1:
            return dp[i]

        skip = self.solve(nums, i + 1, dp)
        steal = nums[i] + self.solve(nums, i + 2, dp)
        dp[i] = max(skip, steal)
        return dp[i]
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        return self.solve(nums, 0, dp)
            

        