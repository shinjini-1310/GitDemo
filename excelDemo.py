import openpyxl as op

book = op.load_workbook("C:\\Users\\SHINJINI\\Imp_Docs\\Selenium Course\\pythonDemo.xlsx")
sheet = book.active
data_dict = {}
cell = sheet.cell(row=1,column=2)
#print(cell.value)
#sheet.cell(row=1,column=2).value = "firstName_altered"
#print(sheet.cell(row=1,column=2).value)
#print("The maximum number of populated rows in the active sheet are")
#print(sheet.max_row)
#print("The maximum number of populated columns in the active sheet are")
#print(sheet.max_column)
#print(sheet['A8'].value)

for row in range(1,sheet.max_row+1):
    if sheet.cell(row=row,column=1).value == "Testcase2":
        for column in range(2,sheet.max_column+1):
            #print(sheet.cell(row=row,column=column).value)
            data_dict[sheet.cell(row=1,column=column).value]=sheet.cell(row=row,column=column).value
#print(data_dict)