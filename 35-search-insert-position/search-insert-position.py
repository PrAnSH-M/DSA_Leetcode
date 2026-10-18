class Solution:
    def searchInsert(self, A: list[int], target: int) -> int:

        N = len(A)
        L = 0
        R = N - 1

        while L <= R:
            M = L + ((R - L) // 2)

            if A[M] == target:
                return M

            elif target > A[M]:
                L = M + 1

            else:
                R = M - 1
            
        return L