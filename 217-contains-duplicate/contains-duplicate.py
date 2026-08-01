class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}

        for i in range(len(nums)):
            mp[nums[i]] = mp.get(nums[i], 0)+1

        for i in mp.values():
            if i > 1:
                return True

        return False