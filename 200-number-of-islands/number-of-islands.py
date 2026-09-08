class Solution:
    def dfs(self, grid:List[List[str]], i: int, j: int, n: int, m: int):

        if (i < 0 or i >= n or j < 0 or j >= m or grid[i][j] is not '1'):
            return

        grid[i][j] = '0'

        self.dfs(grid, i+1, j, n, m)
        self.dfs(grid, i, j+1, n, m)
        self.dfs(grid, i-1, j, n, m)
        self.dfs(grid, i, j-1, n, m)

    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        count = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j, n, m)
        
        return count
        