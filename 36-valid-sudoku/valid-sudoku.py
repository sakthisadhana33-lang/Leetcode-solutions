class Solution(object):
    def isValidSudoku(self, board):
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    continue

                num = board[i][j]
                box_index = (i//3)*3 + (j//3)

                if (num in row[i] or num in col[j] or num in box[box_index]):
                    return False

                row[i].add(num)
                col[j].add(num)
                box[box_index].add(num)

        return True           


        