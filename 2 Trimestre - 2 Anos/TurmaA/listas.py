#        0,  1,   2,      3   ponteiros
lista = [1,'ETE',True,[10,34,8,1]]
#lista = list()
#lista = list
for e in lista:
    if type(e) == list:
        for i in e:
            print(i)
