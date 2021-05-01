from symbol_tables import *

def get_parameters(line):
    paramlist = []
    currlist = line
    if len(line) > 0:
        while len(currlist) > 0:
            paramlist.append(Symbol(currlist[0], currlist[1]))
            currlist.pop(1)
            currlist.pop(0)
            if (len(currlist) > 0):
                currlist = currlist[0]

    return paramlist


'''
[[a, =, hola], ';']
[a , ',' [b , ',' [[a, = ,hola]]]]
'''
def get_variables(type, line):
    line = [item for sublist in line for item in sublist]
    varList = {}
    currSymbol = Symbol()
    currSymbol.set_type(type)
    while line[0] != ';':
        if line[0] == ',':
            line.pop(0)
        elif line[1] == '=':
            currSymbol.set_name(line[0])
            varList[currSymbol] = line[2]
            line.pop(2)
            line.pop(1)
            line.pop(0)
        else:
            currSymbol.set_name(line[0])
            varList[currSymbol] = None
            line.pop(0)
    return varList





