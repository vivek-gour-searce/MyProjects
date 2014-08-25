__author__ = 'vivek.gour'

class game:

    def __init__(self, sudoku1):
        self.sudoku1 = sudoku1

    def sudoku(self):
        self.search((0, 3), "ABC")

    def search(self, row, col):
        for r in range(row):
            for c in col:
                if self.sudoku1[r][c]:
                    self.fillH(self.sudoku1[r][c], row, col, r, c)

    def fillH(self, value, row, col, r, c):
        # horizontal check
        count = 0
        newR = None
        newC = None
        for a in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
            if a not in col:
                for b in range(0, 9):
                    if b in row and b != r:
                        if self.sudoku1[b][a] == value:
                            newR = b
                            newC = a
                            count += 1

        if count == 1:
            if newR in range(0, 3):
                finalR = (xx for xx in range(0, 3) if xx not in [r, newR])
                rowNew = range(3, 9)
            elif newR in range(3, 6):
                finalR = (xx for xx in range(3, 6) if xx not in [r, newR])
                rowNew = range(0, 3) + range(6, 9)
            else:
                finalR = (xx for xx in range(6, 9) if xx not in [r, newR])
                rowNew = range(0, 6)

            if newC in 'DEFGHI':
                colNew = 'ABC'
            elif newC in 'ABCDEF':
                colNew = 'GHI'
            else:
                colNew = 'DEF'
            colList = []
            colList = (colList.append(x) for x in colNew for y in rowNew if self.sudoku1[y][x] == value)

            if len(colList) == 2:
                for c in colNew:
                    if c not in colList and self.sudoku1[finalR][c] != "" and self.sudoku1[finalR][c] != value:
                        self.sudoku1[finalR][c] = value
            if len(colList) == 1:
                colListNew = []
                colListNew = (colListNew.append(c) for c in colNew if c not in colList)
                a = colListNew

                #if self.sudoku1[finalR][colListNew[0]] != "" and


        # vertical check


if __name__=='__main__':
    sudokuu=[   {"A": "", "B": "7", "C": "", "D": "", "E": "1", "F": "4", "G": "", "H": "", "I": ""},
                {"A": "", "B": "", "C": "9", "D": "2", "E": "", "F": "", "G": "", "H": "", "I": "8"},
                {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "7", "I": ""},
                {"A": "3", "B": "", "C": "", "D": "4", "E": "", "F": "2", "G": "", "H": "8", "I": ""},
                {"A": "5", "B": "", "C": "", "D": "", "E": "7", "F": "", "G": "", "H": "", "I": "9"},
                {"A": "", "B": "4", "C": "", "D": "6", "E": "", "F": "9", "G": "", "H": "", "I": "2"},
                {"A": "", "B": "2", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": ""},
                {"A": "7", "B": "", "C": "", "D": "", "E": "", "F": "1", "G": "3", "H": "", "I": ""},
                {"A": "", "B": "", "C": "", "D": "5", "E": "3", "F": "", "G": "", "H": "9", "I": ""}
             ]
    call = game(sudokuu)
    call.sudoku()