#lista = [1,'ETE',True,[10,34,8,1]]
#Último elemento da lista é sempre -1
lista = []
lista.append(1) # novo elemento no final da lista
lista.append('ETE')
print(lista[-1])
lista2 = [5,78,34]#nova lista
lista = lista + lista2 # junção lista
print(lista)
# inserir em qualquer ponteiro
lista.insert(2,'Python')
print(lista)
lista.insert(len(lista), 'Java')# troca -1 por len(lista)
print(lista)