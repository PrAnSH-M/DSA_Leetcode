
class Solution:
    def strStr(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)

        for i in range(n - m + 1):
            for j in range(m):
                if s1[i + j] != s2[j]:
                    break
            else:
                return i

        return -1
