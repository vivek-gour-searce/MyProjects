__author__ = 'vivek.gour'

class game:

    def __init__(self, sudoku1):
        self.sudoku1 = sudoku1

    def sudoku(self):

        g = game(self.sudoku1)
        for index, step in enumerate(self.sudoku1):
            for col in step:
                #print step[col]
                if step[col]!='':
                    if index>5:
                        if col in 'ABC':
                            #print col, index, step[col]
                            rows = [6, 7, 8]
                            frows = []
                            columns = []
                            for m in [6, 7, 8]:
                                for x in self.sudoku1[m]:
                                    if step[col] == self.sudoku1[m][x]:
                                        #print 'found', self.sudoku1[m][x], 'in row', m, 'and col', x
                                        columns.append(x)
                                        frows.append(m)
                            ncolm = findcol(columns)
                            #print 'in row', set(rows) - set(frows) , step[col], 'is not found and in col', ncolm
                            lrows=[i for i in rows if i not in frows]
                            g.put(lrows,ncolm,step[col])
                        elif col in 'DEF':
                            #print col, index, step[col]
                            rows = [6, 7, 8]
                            frows = []
                            columns = []
                            for m in [6, 7, 8]:
                                for x in self.sudoku1[m]:
                                    if step[col] == self.sudoku1[m][x]:
                                        #print 'found', self.sudoku1[m][x], 'in row', m, 'and col', x
                                        columns.append(x)
                                        frows.append(m)
                            ncolm = findcol(columns)
                            #print 'in row', set(rows) - set(frows) , step[col], 'is not found and in col', ncolm
                            lrows=[i for i in rows if i not in frows]
                            g.put(lrows,ncolm,step[col])
                        else:
                            #print col, index, step[col]
                            rows = [6, 7, 8]
                            frows = []
                            columns = []
                            for m in [6, 7, 8]:
                                for x in self.sudoku1[m]:
                                    if step[col] == self.sudoku1[m][x]:
                                        #print 'found', self.sudoku1[m][x], 'in row', m, 'and col', x
                                        columns.append(x)
                                        frows.append(m)
                            ncolm = findcol(columns)
                            #print 'in row', set(rows) - set(frows) , step[col], 'is not found and in col', ncolm
                            lrows=[i for i in rows if i not in frows]
                            g.put(lrows,ncolm,step[col])
                    elif index > 2:
                        if col in 'ABC':
                            #print col, index, step[col]
                            rows = [3, 4, 5]
                            frows = []
                            columns = []
                            for m in [3, 4, 5]:
                                for x in self.sudoku1[m]:
                                    if step[col] == self.sudoku1[m][x]:
                                        #print 'found', self.sudoku1[m][x], 'in row', m, 'and col', x
                                        columns.append(x)
                                        frows.append(m)
                            ncolm = findcol(columns)
                            #print 'in row', set(rows) - set(frows) , step[col], 'is not found and in col', ncolm
                            lrows=[i for i in rows if i not in frows]
                            g.put(lrows,ncolm,step[col])
                        elif col in 'DEF':
                            #print col, index, step[col]
                            rows = [3, 4, 5]
                            frows = []
                            columns = []
                            for m in [3, 4, 5]:
                                for x in self.sudoku1[m]:
                                    if step[col] == self.sudoku1[m][x]:
                                        #print 'found', self.sudoku1[m][x], 'in row', m, 'and col', x
                                        columns.append(x)
                                        frows.append(m)
                            ncolm = findcol(columns)
                            #print 'in row', set(rows) - set(frows) , step[col], 'is not found and in col', ncolm
                            lrows=[i for i in rows if i not in frows]
                            g.put(lrows,ncolm,step[col])
                        else:
                            #print col, index, step[col]
                            rows = [3, 4, 5]
                            frows = []
                            columns = []
                            for m in [3, 4, 5]:
                                for x in self.sudoku1[m]:
                                    if step[col] == self.sudoku1[m][x]:
                                        #print 'found', self.sudoku1[m][x], 'in row', m, 'and col', x
                                        columns.append(x)
                                        frows.append(m)
                            ncolm = findcol(columns)
                            #print 'in row', set(rows) - set(frows) , step[col], 'is not found and in col', ncolm
                            lrows=[i for i in rows if i not in frows]
                            g.put(lrows,ncolm,step[col])
                    else:
                        if col in 'ABC':
                            #print col, index, step[col]
                            rows = [0, 1, 2]
                            frows = []
                            columns = []
                            for m in [0, 1, 2]:
                                for x in self.sudoku1[m]:
                                    if step[col] == self.sudoku1[m][x]:
                                        #print 'found', self.sudoku1[m][x], 'in row', m, 'and col', x
                                        columns.append(x)
                                        frows.append(m)
                            ncolm = findcol(columns)
                            #print 'in row', set(rows) - set(frows) , step[col], 'is not found and in col', ncolm
                            lrows=[i for i in rows if i not in frows]
                            g.put(lrows,ncolm,step[col])


                        elif col in 'DEF':
                            #print col, index, step[col]
                            rows = [0, 1, 2]
                            frows = []
                            columns = []
                            for m in [0, 1, 2]:
                                for x in self.sudoku1[m]:
                                    if step[col] == self.sudoku1[m][x]:
                                        #print 'found', self.sudoku1[m][x], 'in row', m, 'and col', x
                                        columns.append(x)
                                        frows.append(m)
                            ncolm = findcol(columns)
                            #print 'in row', set(rows) - set(frows) , step[col], 'is not found and in col', ncolm
                            lrows=[i for i in rows if i not in frows]
                            g.put(lrows,ncolm,step[col])
                        else:
                            #print col, index, step[col]
                            rows = [0, 1, 2]
                            frows = []
                            columns = []
                            for m in [0, 1, 2]:
                                for x in self.sudoku1[m]:
                                    if step[col] == self.sudoku1[m][x]:
                                        #print 'found', self.sudoku1[m][x], 'in row', m, 'and col', x
                                        columns.append(x)
                                        frows.append(m)
                            ncolm = findcol(columns)
                            #print 'in row', set(rows) - set(frows) , step[col], 'is not found and in col', ncolm
                            lrows=[i for i in rows if i not in frows]
                            g.put(lrows,ncolm,step[col])

        for a, b in enumerate(self.sudoku1):
            for b in self.sudoku1[a]:
                if self.sudoku1[a][b]=='':
                    g.sudoku()


    def find(self, colm, indexno, value):
        self.colm = colm
        self.indexno = indexno
        self.value = value


    def put(self,lrows,colm,num):

        bcol = ''
        lists = {}
        for a in lrows:
            for x in self.sudoku1[a]:
                if x in colm and self.sudoku1[a][x] == '':
                    bcol = bcol + x
        print bcol
        for x, y in enumerate(self.sudoku1):
            for y in self.sudoku1[x]:
                if y in bcol:
                    try:
                        lists[y] = lists[y] + self.sudoku1[x][y]
                    except:
                        lists[y] = self.sudoku1[x][y]

        for y in lists:
            if num in lists[y]:
                lists[y]='True'
            else:
                lists[y]='False'

        if len(lists) == 2:
            if lists==['True','False'] or lists==['False','True']:
                for y in lists:
                    if lists[y] != 'True':
                        for a in lrows:
                            self.sudoku1[a][y]=num

        print self.sudoku1


def findcol(colm):
    length = len(colm)
    if length == 3:
        return ''

    if length == 2:
        if colm[0] in 'ABC':
            if colm[1] in 'DEF':
                return 'GHI'
            else:
                return 'DEF'
        elif colm[0] in 'DEF':
            if colm[1] in 'GHI':
                return 'ABC'
            else:
                return 'GHI'
        elif colm[0] in 'GHI':
            if colm[1] in 'ABC':
                return 'DEF'
            else:
                return 'ABC'

    if length == 1:
        if colm[0] in 'ABC':
            return 'DEFGHI'
        elif colm[0] in 'DEF':
            return 'ABCGHI'
        else:
            return 'ABCDEF'

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