lista = [1, 'ETE', 'Python', 5, 78, 34, 'Java']
#cadastro = [[0,'adjailson',34,'email@gmail.com'],[1]]
# modo simples
for e in lista:
    if type(e) == int:
        print(e)
# modo não tão simples
for p in range(len(lista)):
    if type(lista[p]) == int:
        print(p)