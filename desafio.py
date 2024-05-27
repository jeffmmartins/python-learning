menu ="""
[d] Depositar 
[s] Sacar 
[e] Extrato
[q] Sair

=> """
print(menu)
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite um valor: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Valor do Depósito R$ : {deposito:.2f}\n"
        else:
            print("Desculpa houve um erro na operação")
    
    elif opcao == "s":
        deposito = float(input("Informe o valor do saque: "))

        excedeu_saldo = deposito > saldo

        excedeu_limite = deposito > limite

        excedeu_saque = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo :
            print(" Operação falhou! você não tem saldo suficiente")

        elif excedeu_limite:
            print("Operação falhou! você não tem limite suficiente")
        
        elif excedeu_saque:
            print("Operação falhou! Número maximo de saques excedidos")

        elif deposito > 0 :
            saldo -= deposito
            extrato += f"Saque: R$ {deposito:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido")

    elif opcao == "e":
        print("\n ========================== EXTRATO ======================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")