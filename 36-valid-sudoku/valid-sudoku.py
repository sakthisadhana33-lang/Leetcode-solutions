class Solution(object):
    def isValidSudoku(self, board):

        def box(row, col):
            valid = [1,2,3,4,5,6,7,8,9]
            for i in row:
                for j in col:
                    if board[i][j].isdigit():
                        if int(board[i][j]) in valid:
                            valid.remove(int(board[i][j]))
                        else:
                            return 1
            return 0

        for i in range(9):
            row_seen = {}
            col_seen = {}
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in row_seen:
                        return False
                    row_seen[board[i][j]] = 1

            
                if board[j][i].isdigit():
                    if board[j][i] in col_seen:
                        return False
                    col_seen[board[j][i]] = 1
            
        s = box(range(3), range(3)) 
        s += box(range(3), range(3,6))
        s += box(range(3), range(6,9))
        s += box(range(6,9), range(3))
        s += box(range(6,9), range(3,6))
        s += box(range(6,9), range(6,9))
        s += box(range(3,6), range(3))
        s += box(range(3,6), range(3,6))
        s += box(range(3,6), range(6,9))

        if s == 0:
            return True
        else:
            return False
                    


        