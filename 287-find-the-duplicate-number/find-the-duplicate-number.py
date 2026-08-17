class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = {}

        for val in nums:
            mp[val] = mp.get(val, 0) + 1

        print(mp)

        ans = 0

        for val in mp:
            if mp[val] > 1:
                ans = val

        return ans