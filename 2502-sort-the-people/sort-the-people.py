class Solution:

    def quick_sort(self, nums:list) -> list:
        if len(nums) <= 1:
            return nums
        
        P = nums[-1]

        L = [x for x in nums[:-1] if x[1] >= P[1]]
        R = [x for x in nums[:-1] if x[1] < P[1]]

        L = self.quick_sort(L)
        R = self.quick_sort(R)

        return L + [P] + R

    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:

        paired = list(zip(names, heights))

        paired = self.quick_sort(paired)

        return [name for name, height in paired]
