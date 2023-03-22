import openpyxl

def saveToExcel(data, arr):
    book = openpyxl.Workbook()
    sheet = book.active
    i = 2
    sheet['A1'] = 'Вакансия программиста/зарплата'

    for data in arr:
        if i >= 6:
            sheet['A' + str(i - 4)] = data
        i += 1

    book.save('res.xlsx')
    book.close()