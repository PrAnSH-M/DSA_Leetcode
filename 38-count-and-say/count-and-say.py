class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        say = self.countAndSay(n - 1)
        result = ""

        i = 0
        while i < len(say):
            charac = say[i]
            count = 0

            while i  < len(say) and say[i] == charac:
                count += 1
                i += 1

            result += str(count) + charac

        return result