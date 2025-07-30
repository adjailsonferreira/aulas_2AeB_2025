saldo=1000
while saldo > 1:
    print("Digite: 1-Saldo, 2-Deposito, 3-Saque, 4-Sair")
    opcao=input()
    if opcao=='1':print('Saldo R$',saldo)
    elif opcao=='2':
        deposito = float(input('Digite um valor R$'))
        saldo = saldo + deposito#saldo += deposito
        print('Saldo R$',saldo)
    elif opcao=='3':
        saque = float(input('Digite um valor R$'))
        saldo = saldo - saque#saldo += saque
        print('Saldo R$',saldo)
    elif opcao=='4':break;print(exit(0))
    else:print('Opção inválida!')
