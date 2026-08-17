class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        # a + b + c + d = 0
        # a + b = -(c + d)
        # it same thing
        count = 0

        mp = {}

        for a in nums1:
            for b in nums2:
                target = a + b
                mp[target] = mp.get(target, 0) + 1

        
        for c in nums3:
            for d in nums4:
                target = -(c + d)

                if target in mp:
                    count += mp[target]

        return count

        


        