class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        n = len(changed)

        if n % 2 != 0:
            return []

        changed.sort()

        mp = {}

        final_arr = []

        for i in changed:
            mp[i] = mp.get(i, 0) + 1

        for i in range(n):
            if mp[changed[i]] == 0:
                continue
            # see if i * 2 is not there in mp for that index means it can't be formed as original array
            check = changed[i] * 2
            if mp.get(check, 0) == 0:
                return []
                # break
            # else if its their then add that val in final arr and reduce freq for that val and the current index val
            mp[changed[i]] -= 1
            mp[check] -= 1
            final_arr.append(changed[i])
        
        return final_arr
            



        