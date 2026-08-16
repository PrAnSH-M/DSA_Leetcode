class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        mp = {}

        for a, b in dominoes:
            key = (min(a, b), max(a, b)) # key = (1, 2) (2, 1)

            ans += mp.get(key, 0) # ans = 0 (1) as for now key count is 1

            mp[key] = mp.get(key, 0) + 1 # {1: 2, 2: 2}

        return ans