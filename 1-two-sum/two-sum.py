class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans_list = []
        j = 1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans_list.append(i)
                    ans_list.append(j)
                    break

        return ans_list
