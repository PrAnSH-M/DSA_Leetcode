class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        mp = {}

        for word in strs:

            freq = [0] * 26

            for ch in word:
                index = ord(ch) - ord('a')
                freq[index] += 1

            key = tuple(freq)

            if key not in mp:
                mp[key] = []

            mp[key].append(word)

        return list(mp.values())