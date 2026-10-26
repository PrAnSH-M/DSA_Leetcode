
from functools import cache

class Solution:
    def findAllConcatenatedWordsInADict(
        self, words: list[str]
    ) -> list[str]:

        st = set(words)

        @cache
        def isConcat(word: str) -> bool:
            if word == "":
                return True

            for i in range(1, len(word) + 1):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in st and isConcat(suffix):
                    return True

            return False

        ans = []

        for word in words:
            st.remove(word)

            if isConcat(word):
                ans.append(word)

            st.add(word)

            # Clear cached results because st has changed
            isConcat.cache_clear()

        return ans
