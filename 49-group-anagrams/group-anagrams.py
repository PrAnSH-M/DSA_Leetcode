class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        mp = {}

        for word in strs:
            compare_word = ''.join(sorted(word))

            if compare_word not in mp:
                mp[compare_word] = []
            mp[compare_word].append(word)

        return list(mp.values())
        