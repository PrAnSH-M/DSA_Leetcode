class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        mp = {}


        for row in wall:
            pos = 0

            for i in range(len(row)-1):
                pos += row[i]
                mp[pos] = mp.get(pos, 0) + 1

        if not mp:
            return len(wall)

        max_gap = max(mp.values())
        return len(wall) - max_gap
        