

__author__ = 'vivek.gour'

import time


class NewGame:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def solve(self):
        NG = NewGame(self.puzzle)
        for index, step in enumerate(self.puzzle):
            for steps in step:
                if step[steps] != '':
                    if 6 <= index <= 8:
                        if steps in 'ABC':
                            NG.CheckHorizontal('DEFGHI', 6, 9, 'DEF', 'GHI', index, 0, 3, 3, 6, step[steps])
                            NG.CheckVertical(0, 3, 3, 6, steps, step[steps], 'ABC', 'DEFGHI')
                        elif steps in 'DEF':
                            NG.CheckHorizontal('ABCGHI', 6, 9, 'ABC', 'GHI', index, 0, 3, 3, 6, step[steps])
                            NG.CheckVertical(0, 3, 3, 6, steps, step[steps], 'DEF', 'ABCGHI')
                        elif steps in 'GHI':
                            NG.CheckHorizontal('ABCDEF', 6, 9, 'ABC', 'DEF', index, 0, 3, 3, 6, step[steps])
                            NG.CheckVertical(0, 3, 3, 6, steps, step[steps], 'GHI', 'ABCDEF')

                    elif 3 <= index <= 5:
                        if steps in 'ABC':
                            NG.CheckHorizontal('DEFGHI', 3, 6, 'DEF', 'GHI', index, 0, 3, 6, 9, step[steps])
                            NG.CheckVertical(0, 3, 6, 9, steps, step[steps], 'ABC', 'DEFGHI')
                        elif steps in 'DEF':
                            NG.CheckHorizontal('ABCGHI', 3, 6, 'ABC', 'GHI', index, 0, 3, 6, 9, step[steps])
                            NG.CheckVertical(0, 3, 6, 9, steps, step[steps], 'DEF', 'ABCGHI')
                        elif steps in 'GHI':
                            NG.CheckHorizontal('ABCDEF', 3, 6, 'ABC', 'DEF', index, 0, 3, 6, 9, step[steps])
                            NG.CheckVertical(0, 3, 6, 9, steps, step[steps], 'GHI', 'ABCDEF')

                    elif 0 <= index <= 2:
                        if steps in 'ABC':
                            NG.CheckHorizontal('DEFGHI', 0, 3, 'DEF', 'GHI', index, 3, 6, 6, 9, step[steps])
                            NG.CheckVertical(3, 6, 6, 9, steps, step[steps], 'ABC', 'DEFGHI')
                        elif steps in 'DEF':
                            NG.CheckHorizontal('ABCGHI', 0, 3, 'ABC', 'GHI', index, 3, 6, 6, 9, step[steps])
                            NG.CheckVertical(3, 6, 6, 9, steps, step[steps], 'DEF', 'ABCGHI')
                        elif steps in 'GHI':
                            NG.CheckHorizontal('ABCDEF', 0, 3, 'ABC', 'DEF', index, 3, 6, 6, 9, step[steps])
                            NG.CheckVertical(3, 6, 6, 9, steps, step[steps], 'GHI', 'ABCDEF')

        NG.solve_new()
        NG.filllastone()
        print self.puzzle
        for k, l in enumerate(self.puzzle):
            for m in l:
                if self.puzzle[k][m] == '':
                    NG.solve()

    def CheckVertical(self, p, q, r, s, Col, Number, Col1, Col2):
        temp_a = 9
        temp_b = ''
        count = 0

        for a in range(p, q) + range(r, s):
            for b in Col1:
                if self.puzzle[a][b] == Number:
                    temp_a = a
                    temp_b = b
                    count += 1
                    if count > 1:
                        break

        if count == 1:
            e = []
            count1 = 0
            if temp_a not in range(p, q):
                for c in range(p, q):
                    for d in Col1:
                        if d != Col and d != temp_b and self.puzzle[c][d] == '':
                            e.append(c)
                h = []
                if len(e) == 2:
                    for f in e:
                        for g in Col2:
                            if self.puzzle[f][g] == Number:
                                h.append(f)
                elif len(e) == 1:
                    for f in e:
                        for g in Col2:
                            if self.puzzle[f][g] == Number:
                                break
                            else:
                                count1 += 1
                    if count1 == 6:
                        for f in e:
                            for g in Col1:
                                if g != Col and g != temp_b and self.puzzle[f][g] == '':
                                    list1 = []
                                    list2 = []
                                    if f > 5:
                                        for x in range(6, 9):
                                            for y in Col1:
                                                list1.append(self.puzzle[x][y])
                                        for y in Col2:
                                                list2.append(self.puzzle[f][y])
                                    elif f > 2:
                                        for x in range(3, 6):
                                            for y in Col1:
                                                list1.append(self.puzzle[x][y])
                                        for y in Col2:
                                                list2.append(self.puzzle[f][y])
                                    elif f >= 0:
                                        for x in range(0, 3):
                                            for y in Col1:
                                                list1.append(self.puzzle[x][y])
                                        for y in Col2:
                                                list2.append(self.puzzle[f][y])
                                    if Number not in list1 not in list2:
                                        self.puzzle[f][g] = Number
                if len(h) == 1:
                    for i in e:
                        for j in Col1:
                            if j != Col and j != temp_b and i != h[0]:
                                list1 = []
                                list2 = []
                                if i > 5:
                                    for x in range(6, 9):
                                        for y in Col1:
                                            list1.append(self.puzzle[x][y])
                                    for y in Col2:
                                            list2.append(self.puzzle[i][y])
                                elif i > 2:
                                    for x in range(3, 6):
                                        for y in Col1:
                                            list1.append(self.puzzle[x][y])
                                    for y in Col2:
                                            list2.append(self.puzzle[i][y])
                                elif i >= 0:
                                    for x in range(0, 3):
                                        for y in Col1:
                                            list1.append(self.puzzle[x][y])
                                    for y in Col2:
                                            list2.append(self.puzzle[i][y])
                                if Number not in list1 not in list2:
                                    self.puzzle[i][j] = Number
            elif temp_a not in range(r, s):
                for c in range(r, s):
                    for d in Col1:
                        if d != Col and d != temp_b and self.puzzle[c][d] == '':
                            e.append(c)
                h = []
                if len(e) == 2:
                    for f in e:
                        for g in Col2:
                            if self.puzzle[f][g] == Number:
                                h.append(f)
                elif len(e) == 1:
                    for f in e:
                        for g in Col2:
                            if self.puzzle[f][g] == Number:
                                break
                            else:
                                count1 += 1
                    if count1 == 6:
                        for f in e:
                            for g in Col1:
                                if g != Col and g != temp_b and self.puzzle[f][g] == '':
                                    list1 = []
                                    list2 = []
                                    if f > 5:
                                        for x in range(6, 9):
                                            for y in Col1:
                                                list1.append(self.puzzle[x][y])
                                        for y in Col2:
                                                list2.append(self.puzzle[f][y])
                                    elif f > 2:
                                        for x in range(3, 6):
                                            for y in Col1:
                                                list1.append(self.puzzle[x][y])
                                        for y in Col2:
                                                list2.append(self.puzzle[f][y])
                                    elif f >= 0:
                                        for x in range(0, 3):
                                            for y in Col1:
                                                list1.append(self.puzzle[x][y])
                                        for y in Col2:
                                                list2.append(self.puzzle[f][y])
                                    if Number not in list1 not in list2:
                                        self.puzzle[f][g] = Number
                if len(h) == 1:
                    for i in e:
                        for j in Col1:
                            if j != Col and j != temp_b and i != h[0]:
                                list1 = []
                                list2 = []
                                if i > 5:
                                    for x in range(6, 9):
                                        for y in Col1:
                                            list1.append(self.puzzle[x][y])
                                    for y in Col2:
                                            list2.append(self.puzzle[i][y])
                                elif i > 2:
                                    for x in range(3, 6):
                                        for y in Col1:
                                            list1.append(self.puzzle[x][y])
                                    for y in Col2:
                                            list2.append(self.puzzle[i][y])
                                elif i >= 0:
                                    for x in range(0, 3):
                                        for y in Col1:
                                            list1.append(self.puzzle[x][y])
                                    for y in Col2:
                                            list2.append(self.puzzle[i][y])
                                if Number not in list1 not in list2:
                                    self.puzzle[i][j] = Number

    def CheckHorizontal(self, RemainColm, x, y, Col1, Col2, row, p, q, r, s, Number=''):
        temp_a = ''
        temp_b = 9
        count = 0

        for a in RemainColm:
            for b in range(x, y):
                if self.puzzle[b][a] == Number:
                    temp_a = a
                    temp_b = b
                    count += 1
                    if count > 1:
                        break
        if count == 1:
            e = ''
            count1 = 0
            if temp_a not in Col1:
                for c in Col1:
                    for d in range(x, y):
                        if d != row and d != temp_b and self.puzzle[d][c] == '':
                            e = e + c
                h = ''
                if len(e) == 2:
                    for f in e:
                        for g in range(p, q) + range(r, s):
                            if self.puzzle[g][f] == Number:
                                h = h + f
                elif len(e) == 1:
                    for f in e:
                        for g in range(p, q) + range(r, s):
                            if self.puzzle[g][f] == Number:
                                break
                            else:
                                count1 += 1
                    if count1 == 6:
                        for f in e:
                            for g in range(x, y):
                                if g != row and g != temp_b and self.puzzle[g][f] == '':
                                    list1 = []
                                    list2 = []
                                    if f in 'ABC':
                                        Colx = 'ABC'
                                    elif f in 'DEF':
                                        Colx = 'DEF'
                                    elif f in 'GHI':
                                        Colx = 'GHI'
                                    if g > 5:
                                        for xx in range(6, 9):
                                            for yy in Colx:
                                                list1.append(self.puzzle[xx][yy])
                                        for xx in range(p, q) + range(r, s):
                                            for yy in f:
                                                list2.append(self.puzzle[xx][yy])
                                    elif g > 2:
                                        for xx in range(3, 6):
                                            for yy in Colx:
                                                list1.append(self.puzzle[xx][yy])
                                        for xx in range(p, q) + range(r, s):
                                            for yy in f:
                                                list2.append(self.puzzle[xx][yy])
                                    elif g >= 0:
                                        for xx in range(0, 3):
                                            for yy in Colx:
                                                list1.append(self.puzzle[xx][yy])
                                        for xx in range(p, q) + range(r, s):
                                            for yy in f:
                                                list2.append(self.puzzle[xx][yy])
                                    if Number not in list1 not in list2:
                                        self.puzzle[g][f] = Number
                if len(h) == 1:
                    for i in e:
                        for j in range(x, y):
                            if h != i and j != row and j != temp_b:
                                list1 = []
                                list2 = []
                                if i in 'ABC':
                                    Colx = 'ABC'
                                elif i in 'DEF':
                                    Colx = 'DEF'
                                elif i in 'GHI':
                                    Colx = 'GHI'
                                if j > 5:
                                    for xx in range(6, 9):
                                        for yy in Colx:
                                            list1.append(self.puzzle[xx][yy])
                                    for xx in range(p, q) + range(r, s):
                                        for yy in i:
                                            list2.append(self.puzzle[xx][yy])
                                elif j > 2:
                                    for xx in range(3, 6):
                                        for yy in Colx:
                                            list1.append(self.puzzle[xx][yy])
                                    for xx in range(p, q) + range(r, s):
                                        for yy in i:
                                            list2.append(self.puzzle[xx][yy])
                                elif j >= 0:
                                    for xx in range(0, 3):
                                        for yy in Colx:
                                            list1.append(self.puzzle[xx][yy])
                                    for xx in range(p, q) + range(r, s):
                                        for yy in i:
                                            list2.append(self.puzzle[xx][yy])
                                if Number not in list1 not in list2:
                                        self.puzzle[j][i] = Number
            elif temp_a not in Col2:
                h = ''
                for c in Col2:
                    for d in range(x, y):
                        if d != row and d != temp_b and self.puzzle[d][c] == '':
                            e = e + c
                if len(e) == 2:
                    for f in e:
                        for g in range(p, q) + range(r, s):
                            if self.puzzle[g][f] == Number:
                                h = h + f
                elif len(e) == 1:
                    for f in e:
                        for g in range(p, q) + range(r, s):
                            if self.puzzle[g][f] == Number:
                                break
                            else:
                                count1 += 1
                    if count1 == 6:
                        for f in e:
                            for g in range(x, y):
                                if g != row and g != temp_b and self.puzzle[g][f] == '':
                                    list1 = []
                                    list2 = []
                                    if f in 'ABC':
                                        Colx = 'ABC'
                                    elif f in 'DEF':
                                        Colx = 'DEF'
                                    elif f in 'GHI':
                                        Colx = 'GHI'
                                    if g > 5:
                                        for xx in range(6, 9):
                                            for yy in Colx:
                                                list1.append(self.puzzle[xx][yy])
                                        for xx in range(p, q) + range(r, s):
                                            for yy in f:
                                                list2.append(self.puzzle[xx][yy])
                                    elif g > 2:
                                        for xx in range(3, 6):
                                            for yy in Colx:
                                                list1.append(self.puzzle[xx][yy])
                                        for xx in range(p, q) + range(r, s):
                                            for yy in f:
                                                list2.append(self.puzzle[xx][yy])
                                    elif g >= 0:
                                        for xx in range(0, 3):
                                            for yy in Colx:
                                                list1.append(self.puzzle[xx][yy])
                                        for xx in range(p, q) + range(r, s):
                                            for yy in f:
                                                list2.append(self.puzzle[xx][yy])
                                    if Number not in list1 not in list2:
                                        self.puzzle[g][f] = Number
                if len(h) == 1:
                    for i in e:
                        for j in range(x, y):
                            if h != i and j != row and j != temp_b:
                                list1 = []
                                list2 = []
                                if i in 'ABC':
                                    Colx = 'ABC'
                                elif i in 'DEF':
                                    Colx = 'DEF'
                                elif i in 'GHI':
                                    Colx = 'GHI'
                                if j > 5:
                                    for xx in range(6, 9):
                                        for yy in Colx:
                                            list1.append(self.puzzle[xx][yy])
                                    for xx in range(p, q) + range(r, s):
                                        for yy in i:
                                            list2.append(self.puzzle[xx][yy])
                                elif j > 2:
                                    for xx in range(3, 6):
                                        for yy in Colx:
                                            list1.append(self.puzzle[xx][yy])
                                    for xx in range(p, q) + range(r, s):
                                        for yy in i:
                                            list2.append(self.puzzle[xx][yy])
                                elif j >= 0:
                                    for xx in range(0, 3):
                                        for yy in Colx:
                                            list1.append(self.puzzle[xx][yy])
                                    for xx in range(p, q) + range(r, s):
                                        for yy in i:
                                            list2.append(self.puzzle[xx][yy])
                                if Number not in list1 not in list2:
                                    self.puzzle[j][i] = Number

    def filllastone(self):
        count = 0
        for l in range(9):
            rowstring = ''
            collist = []
            for m in 'ABCDEFGHI':
                rowstring = rowstring + self.puzzle[l][m]
                if self.puzzle[l][m] == '':
                    self.temp_l = l
                    self.temp_m = m
                    collist.append(m)
                    count += 1
            if count == 1:
                for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                    if n not in rowstring:
                        self.puzzle[self.temp_l][self.temp_m] = n

            if count == 2:
                rowstring1 = ''
                rowstring2 = ''
                notinrowstring = ''
                for a in range(9):
                    rowstring1 = rowstring1 + self.puzzle[a][collist[0]]
                    rowstring2 = rowstring2 + self.puzzle[a][collist[1]]
                for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                    if n not in rowstring:
                        notinrowstring = notinrowstring + n

                for n in notinrowstring:
                    if n in rowstring1 not in rowstring2:
                        self.puzzle[l][collist[1]] = n
                    elif n in rowstring2 not in rowstring1:
                        self.puzzle[l][collist[0]] = n

        count = 0

        for m in 'ABCDEFGHI':
            colstring = ''
            rowlist = []
            for l in range(9):
                colstring = colstring + self.puzzle[l][m]
                if self.puzzle[l][m] == '':
                    self.temp_l = l
                    self.temp_m = m
                    rowlist.append(l)
                    count += 1
            if count == 1:
                for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                    if n not in colstring:
                        self.puzzle[self.temp_l][self.temp_m] = n
            if count == 2:
                colstring1 = ''
                colstring2 = ''
                notincolstring = ''
                for a in 'ABCDEFGHI':
                    colstring1 = colstring1 + self.puzzle[rowlist[0]][a]
                    colstring2 = colstring2 + self.puzzle[rowlist[1]][a]
                for n in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                    if n not in colstring:
                        notincolstring = notincolstring + n

                for n in notincolstring:
                    if n in colstring1 not in colstring2:
                        self.puzzle[rowlist[1]][m] = n
                    elif n in colstring2 not in colstring1:
                        self.puzzle[rowlist[0]][m] = n

            count = 0


    def solve_new(self):
        NG = NewGame(self.puzzle)
        NG.lastprog(0, 3, 'ABC', 0, 'DEFGHI', ['A', 'B', 'C'], 3, 6, 6, 9)
        NG.lastprog(0, 3, 'DEF', 0, 'ABCGHI', ['D', 'E', 'F'], 3, 6, 6, 9)
        NG.lastprog(0, 3, 'GHI', 0, 'ABCDEF', ['G', 'H', 'I'], 3, 6, 6, 9)

        NG.lastprog(3, 6, 'ABC', 3, 'DEFGHI', ['A', 'B', 'C'], 0, 3, 6, 9)
        NG.lastprog(3, 6, 'DEF', 3, 'ABCGHI', ['D', 'E', 'F'], 0, 3, 6, 9)
        NG.lastprog(3, 6, 'GHI', 3, 'ABCDEF', ['G', 'H', 'I'], 0, 3, 6, 9)

        NG.lastprog(6, 9, 'ABC', 6, 'DEFGHI', ['A', 'B', 'C'], 0, 3, 3, 6)
        NG.lastprog(6, 9, 'DEF', 6, 'ABCGHI', ['D', 'E', 'F'], 0, 3, 3, 6)
        NG.lastprog(6, 9, 'GHI', 6, 'ABCDEF', ['G', 'H', 'I'], 0, 3, 3, 6)

    def lastprog(self,a,A,B,C,D,E,p,q,r,s):

        list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list9 = []
        count = 0
        rownumber = []
        colnumber = []
        for rows in range(a,A):
            for col in B:
                list2.append(self.puzzle[rows][col])
                if self.puzzle[rows][col] == '':
                    rownumber.append(rows)
                    colnumber.append(col)
                    count += 1
        for l in list1:
            if l not in list2:
                list3.append(l)
        for b in D:
            list4.append(self.puzzle[C][b])
            list5.append(self.puzzle[C+1][b])
            list6.append(self.puzzle[C+2][b])
        for b in range(p,q) + range(r,s):
            list7.append(self.puzzle[b][E[0]])
            list8.append(self.puzzle[b][E[1]])
            list9.append(self.puzzle[b][E[2]])
        for l in list3:
            if l in list4:
                l4 = True
            else:
                l4 = False
            if l in list5:
                l5 = True
            else:
                l5 = False
            if l in list6:
                l6 = True
            else:
                l6 = False

            if l4 == True and l5 == True and l6 == False:
                row = 2
            elif l4 == True and l5 == False and l6 == True:
                row = 1
            elif l4 == False and l5 == True and l6 == True:
                row = 0
            else:
                row = 9

            if l in list7:
                l7 = True
            else:
                l7 = False
            if l in list8:
                l8 = True
            else:
                l8 = False
            if l in list9:
                l9 = True
            else:
                l9 = False

            if l7 == True and l8 == True and l9 == False:
                col = E[2]
            elif l7 == True and l8 == False and l9 == True:
                col = E[1]
            elif l7 == False and l8 == True and l9 == True:
                col = E[0]
            else:
                col = 'J'

            if row == 9 or col == 'J':
                continue
            else:
                self.puzzle[row][col] = l

            listx = {}
            z = 0
            for rows in range(a,A):
                for col in B:
                    if self.puzzle[rows][col] == '':
                        listx[z] = [rows, col]
                        z += 1

        listx1 = []
        listx2 = []
        listx3 = []
        listx4 = []

        if count == 2:
            if rownumber[0] == rownumber[1]:
                for x in range(9):
                    listx1.append(self.puzzle[x][colnumber[0]])
                    listx2.append(self.puzzle[x][colnumber[1]])
                for l in list3:
                    if l in listx1 not in listx2:
                        self.puzzle[rownumber[0]][colnumber[0]] = l
                    elif l in listx2 not in listx1:
                        self.puzzle[rownumber[0]][colnumber[1]] = l
            elif colnumber[0] == colnumber[1]:
                for x in 'ABCDEFGHI':
                    listx3.append(self.puzzle[rownumber[0]][x])
                    listx4.append(self.puzzle[rownumber[1]][x])
                temp_l = ''
                for l in list3:
                    if l in listx3 not in listx4:
                        self.puzzle[rownumber[1]][colnumber[0]] = l
                        self.puzzle[rownumber[0]][colnumber[0]] = temp_l
                    elif l in listx4 not in listx3:
                        self.puzzle[rownumber[0]][colnumber[0]] = l
                        self.puzzle[rownumber[0]][colnumber[0]] = temp_l
                    temp_l = l

if __name__ == '__main__':
    start = time.localtime()
    print start
    sudoku = [{"A": "", "B": "7", "C": "", "D": "", "E": "1", "F": "4", "G": "", "H": "", "I": ""},
              {"A": "", "B": "", "C": "9", "D": "2", "E": "", "F": "", "G": "", "H": "", "I": "8"},
              {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "7", "I": ""},
              {"A": "3", "B": "", "C": "", "D": "4", "E": "", "F": "2", "G": "", "H": "8", "I": ""},
              {"A": "5", "B": "", "C": "", "D": "", "E": "7", "F": "", "G": "", "H": "", "I": "9"},
              {"A": "", "B": "4", "C": "", "D": "6", "E": "", "F": "9", "G": "", "H": "", "I": "2"},
              {"A": "", "B": "2", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": ""},
              {"A": "7", "B": "", "C": "", "D": "", "E": "", "F": "1", "G": "3", "H": "", "I": ""},
              {"A": "", "B": "", "C": "", "D": "5", "E": "3", "F": "", "G": "", "H": "9", "I": ""}
    ]

    G = NewGame(sudoku)
    G.solve()

    end = time.localtime()
    print end

# def filllasttwo(self):
    #     NG = NewGame(self.puzzle)
    #     lists = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    #     for index in range(9):
    #         for value in lists:
    #             for steps in 'ABCDEFGHI':
    #                 if self.puzzle[index][steps] == '':
    #                     if 6 <= index <= 8:
    #                         if steps in 'ABC':
    #                             NG.CheckHorizontal('DEFGHI', 6, 9, 'DEF', 'GHI', index, 0, 3, 3, 6, value)
    #                             NG.CheckVertical(0, 3, 3, 6, steps, value, 'ABC', 'DEFGHI')
    #                         elif steps in 'DEF':
    #                             NG.CheckHorizontal('ABCGHI', 6, 9, 'ABC', 'GHI', index, 0, 3, 3, 6, value)
    #                             NG.CheckVertical(0, 3, 3, 6, steps, value, 'DEF', 'ABCGHI')
    #                         elif steps in 'GHI':
    #                             NG.CheckHorizontal('ABCDEF', 6, 9, 'ABC', 'DEF', index, 0, 3, 3, 6, value)
    #                             NG.CheckVertical(0, 3, 3, 6, steps, value, 'GHI', 'ABCDEF')
    #
    #                     elif 3 <= index <= 5:
    #                         if steps in 'ABC':
    #                             NG.CheckHorizontal('DEFGHI', 3, 6, 'DEF', 'GHI', index, 0, 3, 6, 9, value)
    #                             NG.CheckVertical(0, 3, 6, 9, steps, value, 'ABC', 'DEFGHI')
    #                         elif steps in 'DEF':
    #                             NG.CheckHorizontal('ABCGHI', 3, 6, 'ABC', 'GHI', index, 0, 3, 6, 9, value)
    #                             NG.CheckVertical(0, 3, 6, 9, steps, value, 'DEF', 'ABCGHI')
    #                         elif steps in 'GHI':
    #                             NG.CheckHorizontal('ABCDEF', 3, 6, 'ABC', 'DEF', index, 0, 3, 6, 9, value)
    #                             NG.CheckVertical(0, 3, 6, 9, steps, value, 'GHI', 'ABCDEF')
    #
    #                     elif 0 <= index <= 2:
    #                         if steps in 'ABC':
    #                             NG.CheckHorizontal('DEFGHI', 0, 3, 'DEF', 'GHI', index, 3, 6, 6, 9, value)
    #                             NG.CheckVertical(3, 6, 6, 9, steps, value, 'ABC', 'DEFGHI')
    #                         elif steps in 'DEF':
    #                             NG.CheckHorizontal('ABCGHI', 0, 3, 'ABC', 'GHI', index, 3, 6, 6, 9, value)
    #                             NG.CheckVertical(3, 6, 6, 9, steps, value, 'DEF', 'ABCGHI')
    #                         elif steps in 'GHI':
    #                             NG.CheckHorizontal('ABCDEF', 0, 3, 'ABC', 'DEF', index, 3, 6, 6, 9, value)
    #                             NG.CheckVertical(3, 6, 6, 9, steps, value, 'GHI', 'ABCDEF')
