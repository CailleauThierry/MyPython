from __future__ import print_function
import openpyxl as wb

wb1 = wb.load_workbook('C:\Users\Administrator\Downloads\Example.xlsx')
ws1 = wb1.get_sheet_by_name('Raw Data - MTD_5')
res1 = ws1['O3'].value
res2 = ws1.cell(row=3, column=12).value

print(res1)
print(res2)

#this does display the value of Raw 3 Column O and raw 3 Column L (i.e. column 12) even is the content of column 12 is a long text string

