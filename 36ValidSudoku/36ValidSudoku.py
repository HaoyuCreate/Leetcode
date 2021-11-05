class Solution:
    def isValidSudoku(self, board) -> bool:
        import numpy as np
        board = np.array(board)
        for row in board:
            if not self.CheckValid(row):
                return False

        for i in range(len(board[0])):
            col = list(board[:,i])
            if not self.CheckValid(col):
                return False

        for i in range(9):
            grid_x = int(i % 3) * 3
            grid_y = int(i / 3) * 3
            block = self.BlockToList(board,grid_x,grid_y)
            if not self.CheckValid(block):
                return False
        return True

    def CheckValid(self,List):
        newList = list(filter(('.').__ne__,List)) #O(n)
        if len(newList) == len(set(newList)): #O(1)
            return True
        else:
            return False

    def BlockToList(self,board,grid_x,grid_y):
        result = []
        mat = board[grid_y:grid_y+3]
        for row in mat:
            result.extend(row[grid_x:grid_x+3])
        return result



if __name__=='__main__':
    solution = Solution()
    l1 = [["5","3",".","7","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]
    print(solution.isValidSudoku(l1))