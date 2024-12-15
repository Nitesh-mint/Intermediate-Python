
class Sudoku:
    def __init__(self, board):
        self.board = board

    def check_nums_cell(self, square):
        print(square)

    def find_empty_cell(self):
        #Iterating through row
        for i in range(9):
            #Iterating through column
            for j in range(9):
                if self.board[i][j] == 0:
                    print(i, j)
        return None


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
s = Sudoku(board)
print(s.find_empty_cell())
