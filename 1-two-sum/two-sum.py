class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ans = []

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             ans.append(i)
        #             ans.append(j)
        #             break

        # return ans

        mp = {}

        for index, val in enumerate(nums):
            comp = target - val

            if comp in mp:
                return [mp[comp], index]

            mp[val] = index

        return mp


