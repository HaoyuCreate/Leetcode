class Solution:
    def numIslands(self, grid) -> int:
        h = len(grid)
        w = len(grid[0])
        stack = []
        nums_islands = 0

        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    nums_islands += 1
                    stack.append((i, j))
                    grid[i][j] = "2"
                    while stack:
                        (i, j) = stack.pop()

                        self.checkIsland(grid, stack, i + 1, j)
                        self.checkIsland(grid, stack, i - 1, j)
                        self.checkIsland(grid, stack, i, j + 1)
                        self.checkIsland(grid, stack, i, j - 1)
        return nums_islands

    def checkIsland(self, grid, stack, i, j):
        if (0 <= i and i < len(grid) and 0 <= j and j < len(grid[0])) and grid[i][j] == "1":
            grid[i][j] = "2"
            stack.append((i, j))

    # def numIslands2(self, grid) -> int:
    #     h = len(grid)
    #     w = len(grid[0])
    #     nums_islands = 0
    #     # visited = [][]
    #     # visited island <-> '2'
    #     for i in range(h):
    #         for j in range(w):
    #             if grid[i][j] == "1":
    #                 nums_islands += 1
    #                 self.dsf(grid, i, j)
    #     return nums_islands
    #
    # def dsf(self, grid, i, j):
    #     h, w = len(grid), len(grid[0])
    #     if not self.inArea(grid, i, j, h, w):
    #         return
    #
    #     if grid[i][j] != "1":
    #         return
    #
    #     grid[i][j] = "2"
    #
    #     self.dsf(grid, i + 1, j)
    #     self.dsf(grid, i - 1, j)
    #     self.dsf(grid, i, j + 1)
    #     self.dsf(grid, i, j - 1)
    #
    # def inArea(self, grid, i, j, h, w):
    #     return (0 <= i and i < h and 0 <= j and j < w)


    # def numIslands3(self, grid) -> int:
    #     # 深度优先搜索：
    #     island_num = 0
    #
    #     if not grid:
    #         return island_num
    #
    #     m, n = len(grid), len(grid[0])
    #
    #     for i in range(m):
    #         for j in range(n):
    #
    #             if grid[i][j] != "0":
    #                 island_num += 1
    #                 stack = [[i, j], ]
    #
    #                 while stack:
    #
    #                     [p, q] = stack.pop()
    #
    #                     if p > 0 and grid[p - 1][q] == "1":
    #                         stack.append([p - 1, q])
    #                     if p < m - 1 and grid[p + 1][q] == "1":
    #                         stack.append([p + 1, q])
    #                     if q > 0 and grid[p][q - 1] == "1":
    #                         stack.append([p, q - 1])
    #                     if q < n - 1 and grid[p][q + 1] == "1":
    #                         stack.append([p, q + 1])
    #
    #                     grid[p][q] = "0"
    #
    #     return island_num

sol = Solution()
#inputs = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
inputs = [["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]]
print(sol.numIslands(inputs))
# print(sol.numIslands2(inputs))