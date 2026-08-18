class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mp = {}

        for i in nums:
            mp[i] = mp.get(i, 0)+1

        print(mp)
        
        min_miss = 1

        while min_miss in mp:
            min_miss += 1
        
        return min_miss
