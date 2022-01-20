import xlrd
from TSP import city


def input_city():
    book = xlrd.open_workbook('eil51tsp.xlsx')  # 打开一个excel
    # book = xlrd.open_workbook('pr439tsp.xlsx')  # 打开一个excel
    sheet = book.sheet_by_index(0)  # 根据顺序获取sheet
    citys = []
    for i in range(sheet.nrows):  # 0 1 2 3 4 5
        if i == 0:
            continue
        row = sheet.row_values(i)
        t = city.city(row[0], row[1], row[2])
        citys.append(t)
        pass
    # N = sheet.nrows - 1
    return citys