class Solution:

    def pivot_idx(self, nums: list[int]) -> int:
        L = 0
        R = len(nums) - 1

        while L < R:
            M = L + (R - L) // 2

            if nums[M] > nums[M + 1]:
                return M

            if nums[M] < nums[R]:
                R = M
            else:
                L = M + 1

        return L


    def bs(self, nums: list[int], L: int, R: int, target: int) -> int:

        N = len(nums)
        
        while L <= R:
            M = L + (R - L) // 2
            if nums[M] == target:
                return M
            elif nums[M] < target:
                L = M + 1
            else: R = M - 1

        return -1


    def search(self, nums: list[int], target: int) -> int:

        N = len(nums)
        
        """

        as we seeing array is rotated sorted means it can be in rotated sorted at any index K 
        what i am thinking is 


        nums = [ 4 ,5 ,6 ,7 ,0 ,1 ,2 ]

           finding a pivot point where we can use binary search as first half including Pivot and second half without pivot 

           because if take pivot point as 7 we can see first half is small (ascending sort) including pivot and sec part also in asc  


        """

        pivot = self.pivot_idx(nums)


        b_s_including_pivot_idx = self.bs(nums, 0, pivot, target)
        if b_s_including_pivot_idx != -1:
            return b_s_including_pivot_idx

        return self.bs(nums, pivot + 1, N - 1, target)

        