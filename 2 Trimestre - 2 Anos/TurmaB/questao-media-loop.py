#Desenvolver uma função 'split' melhorada:
def _split(sequencia)-> list:
    lista = []
    for e in sequencia:
        lista.append(e)
    return lista

def contido(escolher, sequencia):
    for i in sequencia:
        for j in escolher:
            if i == j:
                return True
    return False

# Registro de notas de vários alunos e no final mostre a média
contador = 0
soma_notas = 0
while True:
    resposta = input(f'Digite a nota {contador+1}:')

    if contido(resposta,"medianão"):
        break
    else:
        soma_notas += float(resposta)
        contador = contador + 1# contador += 1
print('Média é',soma_notas/contador)