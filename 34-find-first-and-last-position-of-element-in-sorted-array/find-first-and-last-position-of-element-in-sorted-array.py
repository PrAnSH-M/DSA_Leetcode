class Solution:

    def bs(self, A: list[int], L:int, R:int, target: int, first_found: bool) -> int:
        N = len(A)
        ans = -1

        while L <= R:
            M = L + ((R-L) // 2)

            if A[M] == target:
                ans = M

                if first_found:
                    R = M - 1
                else:
                    L = M + 1
            
            elif A[M] < target:
                L = M + 1
            else:
                R = M - 1

        return ans



    def searchRange(self, nums: list[int], target: int) -> list[int]:
        N = len(nums)
        ans = [-1]*2

        first = self.bs(nums, 0, N-1, target, True)
        second = self.bs(nums, 0, N-1, target, False)

        ans[0] = first
        ans[1] = second

        return ans
        