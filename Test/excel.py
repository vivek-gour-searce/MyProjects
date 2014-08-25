__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2013, Searce'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Vivek.Gour@searce.com'
__status__ = 'Development'


from xlrd import open_workbook, cellname, XL_CELL_TEXT, empty_cell

path = "D/programs/Vivek/daybookF/"
book = open_workbook('D:\programs\Vivek\daybookF\PH-DayBookF02-Jun-2014-031426.xls')

print book.nsheets
print book.sheet_names()


sheet = book.sheet_by_index(0)

sheet0 = book.sheet_by_index(0)

print empty_cell.value
empty = sheet.cell(6, 2)
blank = sheet.cell(7, 2)
print empty is blank, empty is empty_cell, blank is empty_cell

print empty.ctype, repr(empty.value)
print blank.ctype, repr(blank.value)

# print sheet0.row(0)
# print sheet0.col(0)
# print
# print sheet0.row_slice(0, 1)
# print sheet0.row_slice(0, 1, 2)
# print sheet0.row_values(0, 1)
# print sheet0.row_values(0, 1, 2)
# print sheet0.row_types(0, 1)
# print sheet0.row_types(0, 1, 2)

# for sheet_index in range(book.nsheets):
#     print book.sheet_by_index(sheet_index)
#
# for sheet_name in book.sheet_names():
#     print book.sheet_by_name(sheet_name)
#
# for sheet in book.sheets():
#     print sheet


# print sheet.name
#
# print sheet.nrows
# print sheet.ncols

# for row_index in range(sheet.nrows):
#     for col_index in range(sheet.ncols):
#         print cellname(row_index, col_index), '-',
#         print sheet.cell(row_index,col_index).value
#
# sheet = book.sheet_by_index(0)
# cell = sheet.cell(0,0)
# print cell
# print cell.value
# print cell.ctype==XL_CELL_TEXT
#
# for i in range(sheet.ncols):
#     print sheet.cell_type(1,i),sheet.cell_value(1,i)


