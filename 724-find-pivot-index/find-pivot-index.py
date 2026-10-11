class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)

        carry = [0] * n

        carry[0] = nums[0]

        for i in range(1, n):
            carry[i] += carry[i-1] + nums[i]
        
        # print("carry arrar ->",carry)
        
        total_sum = 0
        for i in range(n):
            total_sum += nums[i]
        
        # print("total_sum ->",total_sum)

        for i in range(n):

            if i == 0:
                left_sum = 0
            
            else:
                left_sum = carry[i-1]

            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:
                return i
            
        return -1