class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0: 1}
        count = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num

            diff = curr_sum - k

            if diff in mp:
                count += mp[diff]

            mp[curr_sum] = mp.get(curr_sum, 0) + 1

        return count 
        