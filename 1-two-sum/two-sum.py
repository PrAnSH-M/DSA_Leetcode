class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mp = {}

        output = []

        for i in range(len(nums)):
            complement = target - nums[i] # 9 - 2
            if complement in mp: 
                output.append(mp[complement])
                output.append(i)
                return output
            mp[nums[i]] = i # {7, 2}
            # print(mp)
        
        return output

        