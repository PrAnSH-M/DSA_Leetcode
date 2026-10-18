class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0
        l = 1
        r = x
        ans = 1

        while l <= r:
            m = l + ((r - l) // 2)
            m_square = m*m

            if m_square > x:
                r = m - 1

            else:
                ans = m
                l = m + 1
            
        
        return ans
        