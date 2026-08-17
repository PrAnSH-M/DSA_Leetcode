class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()

        for i in range(len(s)-k+1):
            substring = s[i: i+k]
            # print(substring)
            seen.add(substring)
            # print(seen)

        return len(seen) == 2**k
