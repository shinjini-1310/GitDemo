#THIS IS THE ALTERED VERSION OF THE CODE DOWNLOADED/CLONED FROM ORIGINAL CODE IN REMOVE GITHUB REPO

import openpyxl as op

book = op.load_workbook("C:\\Users\\SHINJINI\\Imp_Docs\\Selenium Course\\pythonDemo.xlsx")
sheet = book.active
data_dict = {}
cell = sheet.cell(row=1,column=2)

for row in range(1,sheet.max_row+1):
    if sheet.cell(row=row,column=1).value == "Testcase2":
        for column in range(2,sheet.max_column+1):
            #print(sheet.cell(row=row,column=column).value)
            data_dict[sheet.cell(row=1,column=column).value]=sheet.cell(row=row,column=column).value
print("THIS IS THE ALTERED VERSION OF THE CODE DOWNLOADED/CLONED FROM ORIGINAL CODE IN REMOVE GITHUB REPO")