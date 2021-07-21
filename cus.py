import datetime


def respprint(obj):
    keys = obj[0].keys()
    for item in keys:
        print("{0:20s}".format(item), end='')
    for item in obj:
        for element in item:
            print("{0:20s}".format(str(item[element])), end='')
        print()
# order = admin.getorders() i respprint(order) --- def
