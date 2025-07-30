'''
Pedi notas
infinito
'''
contador = 0
notas = 0
while True:# loop infinito
    # pedir a nota ao usuário e realizar as soma:
    #notas = notas + float(input("Digite uma nota"))
    # verificar o conteudo da variável:
    resposta = input("Digite uma nota:")
    if len(resposta) > 3:# Então, parar
        break
    else:
        contador = contador + 1
        notas += float(resposta)#notas = notas + float(resposta)
print('Média das notas =',notas/contador)