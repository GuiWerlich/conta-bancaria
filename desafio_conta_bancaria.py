#realizar um sistema implementando as funções: depósito, saque e extrato.

#depósito: sempre depositar valores positivos, zero e negativo são invalidos; os depósitos devem ser armazenados em uma variavel e exibidos no extrato.
#saque: limite de 3 saques com um limite maximo de 500 reais. se a conta estiver vazia exibir. saques devem ser armazenados e exibidos no extrato.
#extrato: deve exibir todos os dep e saq feitos. no fim da listagem deve exibir o saldo atual.

menu = ''' ------BEM VINDO AO BANCO WERLICH------

1 - DEPOSITAR
2 - SACAR
3 - EXTRATO
0 - SAIR

Digite a opção desejada: 
'''

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = (input(menu))

    if opcao == "1":
        deposito = float(input('Digite o valor que deseja depositar: '))
        if deposito > 0:
            saldo = saldo + deposito
            print(f'Seu depósito no valor de R$ {deposito:.2f} foi realizado com sucesso!')
        else:
            print('Digite um valor valido!')
    elif opcao == "2":
        saque = float(input('Digite o valor que deseja sacar: '))
        if numero_saques != LIMITE_SAQUES:
            if saldo <= 0:
                print('Voce não possui saldo suficiente para essa operação!')
            elif saldo > 0 and saque > limite:
                print(f'Seu limite de saque é de R${limite:.2f}')
            else:
                saldo = saldo - saque
                print(f'Seu saque no valor de R${saque:.2f} foi realizado com sucesso!')
                numero_saques = numero_saques + 1
        else:
            print('Voce atingiu o limite de saques diário. Tente novamente amanhã')
    elif opcao == "3":
        print(f'Seu saldo atual é de R${saldo:.2f}.') 
    elif opcao == "0":
        print("Obrigado por utilizar nosso sistema. Até mais!")
        break
    else:
        print('Digite uma opção valida!')
