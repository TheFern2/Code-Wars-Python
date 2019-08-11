
class Cell:
    def __init__(self, cell):
        self.row = 0
        self.col = 0
        self.calculate_row(cell[0])
        self.calculate_col(cell[1])

    def calculate_row(self, row):
        if "A" in row:
            self.row = 0
        if "B" in row:
            self.row = 1
        if "C" in row:
            self.row = 2
        if "D" in row:
            self.row = 3
        if "E" in row:
            self.row = 4
        if "F" in row:
            self.row = 5
        if "G" in row:
            self.row = 6
        if "H" in row:
            self.row = 7

    def calculate_col(self, col):
        self.col = int(col) -1


def chess_board_cell_color(cell1, cell2):
    n = 8

    board = [["BW"[(i+j+n%2+1) % 2] for i in range(n)] for j in range(n)]

    cellone = Cell(cell1)
    celltwo = Cell(cell2)

    if board[cellone.row][cellone.col] == board[celltwo.row][celltwo.col]:
        return True
    else:
        return False