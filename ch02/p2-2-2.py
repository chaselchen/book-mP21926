import pprint as pp
filename = 'ch02/info.csv'
data = list()
with open(filename, 'rt') as fp:
    columns = fp.readline().split(",")
    for item in fp.readlines():
        temp = dict()
        for i, field in enumerate(item.split(",")):
            temp[columns[i].strip()] = field.strip()
        data.append(temp)
# pp.pprint(data)

def test():
    print('my test')
    data = []
    with open(filename, 'rt') as fp:
        columns = fp.readline().split(',')
        for item in fp.readlines():
            temp = {}
            for i, field in enumerate(item.split(',')):
                temp[columns[i].strip()] = field.strip()
            
            data.append(temp)
    
    pp.pprint(data)


test()