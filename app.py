# Libraries
from os import listdir
from openpyxl import load_workbook, workbook
import unidecode

# Path
bancoGeneral = './CSV'

#Files
files = listdir(bancoGeneral)

def budget():
    #Load Excel
    listFiles = []

    for f in files:
        workbook = load_workbook(filename=f'{bancoGeneral}/{f}')
        colums = ['A', 'C', 'D', 'E', 'F', 'H', 'I']
        sheet = workbook.active
        #title
        account = sheet['A4'].value
        #Init and last Row of items
        initialRow = [i+1 for i, j in enumerate(sheet['A']) if j.value == 'Fecha'][0]
        lastRow = len(sheet['A']) - initialRow
        print(f'inicias:{initialRow} | fin: {lastRow} | total: {lastRow - initialRow}')
        # Row Table
        properties = {
            "account": account,
            "items":[]
        }

        # Iterate initial value data below Column - Vertically
        for x in range(initialRow + 1, lastRow):
            # print(f'{x}')

            # Iterate Horizontally
            for i, data in enumerate(colums):
                # print(f'{data}{x}')
                # print(sheet[f'{data}{x}'].value)
                if sheet[f'{data}{x}'].value != None:
                    properties['items'].append({
                        cleanProperties(sheet[f'{data}{initialRow}'].value):str(sheet[f'{data}{x}'].value),
                    })
        print(properties)

def cleanProperties(value):
    value = unidecode.unidecode(value)
    return value.replace(' ', '-').lower()
    
# Exec main function
budget()