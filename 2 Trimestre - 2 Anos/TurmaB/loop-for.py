
def remover_espaco(frase):
    temp = ""
    for letra in frase:
        if not(letra==' '):
            temp += letra
    return temp

print(remover_espaco('ETE  Ariano Vilar    '))
# O 'for' é usado para conjuntos de dados
for numero in range(10):# interagir com 10 valores
    print(numero)

#interação sobre letras e caracteres:  
palavra = "ETE Ariano"

for e in range(len(remover_espaco(palavra))):
    print(e)

#interação direta entre frases ou palavras
for letra in palavra:
    print(letra, end=',')
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