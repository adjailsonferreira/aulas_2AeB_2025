# Declaração de lista
lista = [1,'ETE',['A','B','C'],True,[3,78,9],[1,2,3,4]]
#lista = list()
#Acesso
print(lista[1])
#Último
print(lista[-1])
print(lista[len(lista)-1])
#Inserir/adicionar
lista.append(2025)
print(lista)
contador = 0
for e in lista:
    if type(e) == list:
        contador += 1
        if contador == 2:
            print(e)
            break
