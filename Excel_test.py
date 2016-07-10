from __future__ import print_function
import openpyxl as wb

wb1 = wb.load_workbook('C:\Users\Administrator\Downloads\Example.xlsx')
ws = wb1.get_sheet_by_name('Raw Data - MTD_5')
print(ws)

#results:
#C:\Anaconda2\python.exe C:/Users/Administrator/PycharmProjects/Excel/excel_test.py
#[u'CSAT by Month_1', u'Overall CSAT Results_2', u'CSAT by KCRP - MTD_3', u'CSAT by Agent - MTD_4', u'Raw Data - MTD_5']
#
#Process finished with exit code 0