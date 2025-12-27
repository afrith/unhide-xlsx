#!/usr/bin/env python3
import openpyxl
import sys

def unhide_sheets(filename):
    wb = openpyxl.load_workbook(filename)
    for sheet in wb.worksheets:
        sheet.sheet_state = 'visible'
    outfile = filename.replace('.xlsx', '_unhidden.xlsx')
    wb.save(outfile)

if __name__ == "__main__":
  unhide_sheets(sys.argv[1])