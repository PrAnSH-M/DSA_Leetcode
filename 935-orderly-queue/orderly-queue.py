class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:

        if k > 1:
            s = ''.join(sorted(s))
            return s
        
        ans = s
        n = len(s)
        for i in range(1, n):
            temp = s[i:] + s[:i]
            ans = min(ans, temp)
        
        return ans
            
        