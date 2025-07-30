
'''
Loops em Python
while e for
'''
'''
#O while ele tem que ter condição
# de parada para uso break OU um contador
'''
#Parar pelo contador
contador = 0
while contador < 10:
    print(contador)
    contador = contador + 1
print('fim')

#Parar pelo break
while True:
    nota = float(input('Digite uma nota:'))
    if nota < 0 or nota > 10:break

#Uso do contador, mas não para uso de parada
# Registro de notas de vários alunos e no final mostre a média
contador = 0
soma_notas = 0
while True:
    resposta = input(f'Digite a nota {contador+1}:')

    if len(resposta) > 4:
        break
    else:
        soma_notas += float(resposta)
        contador = contador + 1# contador += 1
print('Média é',soma_notas/contador)