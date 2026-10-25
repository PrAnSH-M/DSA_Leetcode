
class Solution:
    def makeGood(self, s: str) -> str:
        result = ""

        for ch in s:
            if result and abs(ord(result[-1]) - ord(ch)) == 32:
                result = result[:-1]
            else:
                result += ch

        return result
