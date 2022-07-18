import pprint as pp
import json
filename = 'ch02/jdata.json'
with open(filename, "rt") as fp:
    data = json.loads(fp.read())
# pp.pprint(data)

def test():
    with open(filename, "rt") as fp:
        data = json.loads(fp.read())

    pp.pprint(data)
    

test()