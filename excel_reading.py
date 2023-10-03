# xlrd - reading of excel files
# .xlsx, .xls
# pip install xlrd==1.2.0

# workbook --> worksheets -> rows/columns/cell

from xlrd import open_workbook

# # create an instance of open workbook
# workbook = open_workbook("sample_data.xlsx")
#
# # open the worksheet
# worksheet = workbook.sheet_by_name("Sheet1")
#
# # reads the rows present in the work sheet
# rows = worksheet.get_rows()        # generator object
# print(rows)
#
# # skipping the header
# header = next(rows)              # reads the first element from the rows

# # reading the rows as list of cell objects
# for row in rows:
# 	print(row)          # list of cell objects

# # reading the rows as list of values
# for row in rows:
# 	print([row[0].value, row[1].value])

# # reading the data as dictionary
# data = {}
# for row in rows:
# 	data[row[0].value] = row[1].value
# print(data)
#
#
# # re-initializing the generator object
# rows = worksheet.get_rows()
# header = next(rows)
#
# data = {row[0].value: row[1].value for row in rows}
# print(data)

######################################################################################
# creating an instance of workbook
wb = open_workbook("sample_data.xlsx")

# creating an instance of worksheet
ws = wb.sheet_by_name("Sheet2")

# collecting entire rows from the worksheet
rows = ws.get_rows()

# skipping the header
header = next(rows)

# # reading the data as a list
# data = []
# for row in rows:
# 	row_data = (row[0].value, row[1].value, row[2].value)
# 	data.append(row_data)
#
# print(data)

# reading the data as dictionary
data = {}
for row in rows:
	data[row[0].value] = (row[1].value, row[2].value)

# print(data)

#################################################################################
print(ws.ncols)         # number of used columns
print(ws.nrows)         # number of used rows





