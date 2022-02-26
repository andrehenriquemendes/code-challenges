# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or c >= cols or r >= rows:
                return

            if grid[r][c] == '0' or grid[r][c] == '-1':
                return

            grid[r][c] = '-1'  # visited

            dfs(r - 1, c)  # below
            dfs(r + 1, c)  # above
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right

        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c)

        return num_islands