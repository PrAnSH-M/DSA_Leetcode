class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        mp = {}
        """
            our map will contain number as key and index as value
            if we found dup we will do abs that current number idx with idx stored in mp if its != K
            will update index in mp for that number if its <= K then return true and if loop over at the end
            return false
        """

        for i in range(n):

            if nums[i] not in mp:
                mp[nums[i]] = i
            else:
                if abs(mp.get(nums[i]) - i) <= k:
                    return True 
            
                mp[nums[i]] = i
        
        return False

        