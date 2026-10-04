class Solution:
    final : List[List[int]] = []

    def twoSum(self, nums: List[int], target: int, i: int, j:int):
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                # first remove duplicates
                while i < j and nums[i] == nums[i+1]:
                    i+=1
                while i < j and nums[j] == nums[j-1]:
                    j -= 1
                self.final.append([-target, nums[i], nums[j]])

                i += 1
                j -= 1

                


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        if n < 3:
            return []

        self.final.clear()

        # n1
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            n1 = nums[i]
            target = -n1

            self.twoSum(nums, target, i+1, n-1) # find n2 and n3

        return self.final


        