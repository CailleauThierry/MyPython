from __future__ import print_function
import openpyxl as wb

wb1 = wb.load_workbook('C:\Users\Administrator\Downloads\Example.xlsx')
ws1 = wb1.get_sheet_by_name('Raw Data - MTD_5')
res1 = ws1['O2'].value
res2 = ws1.cell(row=2, column=15).value

print(res1)
print(res2)

#this does display the value of Raw 2 Column O in 2 different fashion

