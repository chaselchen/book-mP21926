import xlrd
filename = "ch02/scores.xlsx"

data = xlrd.open_workbook(filename)
s1 = data.sheets()[0]
s2 = data.sheets()[1]

print(data)
print(s1)
print(s2)