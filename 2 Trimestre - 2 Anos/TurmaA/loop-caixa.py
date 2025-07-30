saldo = 10000
saque = 0
palavra = "um"
while True:
    opcao = input(f'Deseja realizar {palavra} saque?').lower()
    if opcao == 'sim' or opcao == '':
        saque = int(input('Qual o valor R$:'))
        if saque >= 200:
            qtd_notas = saque//200
            print('Notas de 200 =',qtd_notas)
            saque = saque - (qtd_notas * 200)
            saldo = saldo - (qtd_notas * 200)
        if saque >= 100:
            qtd_notas = saque//100
            print('Notas de 100 =',qtd_notas)
            saque = saque - (qtd_notas * 100)
            saldo = saldo - (qtd_notas * 100)
        palavra = "outro"
    else:break
print('Saldo atual R$',saldo)
print('Troco R$',saque)