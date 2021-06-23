import openpyxl as xls
import glob

def getBeginRow(bk) :
    row = 1
    row_begin_data = 1

    while sh.cell(row, 1).value != "告示番号" :
        row += 1

    row += 1
    return row

# main -----------------------

files = glob.glob("d:/xls/*.xlsx")

for file in files:
    bk = xls.load_workbook(file)
    sh = bk.worksheets[0]

    row_begin_data = getBeginRow(bk)

    print(file + " ---> " + str(row_begin_data))
