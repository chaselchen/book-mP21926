filename = 'ch02/info.csv'
with open(filename, 'rt') as fp:
    data = fp.readlines()
print(data)


with open(filename) as fp:
    data = fp.readlines()

print(data)