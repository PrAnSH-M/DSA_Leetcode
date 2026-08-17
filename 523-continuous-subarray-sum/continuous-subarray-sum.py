class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0: -1}
        curr_sum = 0
        index = 0

        ans = False

        for num in nums:
            curr_sum += num

            remainder = curr_sum % k

            if remainder in mp:
                if index - mp[remainder] >= 2:
                    ans = True
            else:
                mp[remainder] = index
            index += 1
        return ans
        