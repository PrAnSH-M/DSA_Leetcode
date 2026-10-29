class Solution:

    def checkFreq(self, s: str, goal: str) -> bool:
        mp = {}

        for ch in s:
            mp[ch] = mp.get(ch, 0)+1
        
        for count in mp.values():
            if count > 1:
                return True

        return False
                

    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        if s == goal:
            return self.checkFreq(s, goal)

        indices = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                indices.append(i)

        if len(indices) != 2:
            return False

        i, j = indices

        return s[i] == goal[j] and s[j] == goal[i]

        