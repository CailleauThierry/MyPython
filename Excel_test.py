from __future__ import print_function
import openpyxl as wb

wb1 = wb.load_workbook('C:\Users\Administrator\Downloads\Example.xlsx')
ws1 = wb1.get_sheet_by_name('Raw Data - MTD_5')
res1 = ws1['A1'].value
print(res1)

#this does display the value of Raw 1 Column A