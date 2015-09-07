__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2013, Searce'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Vivek.Gour@searce.com'
__status__ = 'Development'


class new():
    def __init__(self):
        self.sudoku = [["", "7", "", "", "1", "4", "", "", ""],
                       ["", "", "9", "2", "", "", "", "", "8"],
                       ["", "", "", "", "", "", "", "7", ""],
                       ["3", "", "", "4", "", "2", "", "8", ""],
                       ["5", "", "", "", "7", "", "", "", "9"],
                       ["", "4", "", "6", "", "9", "", "", "2"],
                       ["", "2", "", "", "", "", "", "", ""],
                       ["7", "", "", "", "", "1", "3", "", ""],
                       ["", "", "", "5", "3", "", "", "9", ""]]

    def solve(self):

        for row in self.sudoku:
            for col in row:
                print col




c = new()
c.solve()