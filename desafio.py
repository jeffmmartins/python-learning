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
        print("saque realizado")

    elif opcao == "e":
        print("segue extrato")
    
    elif opcao == "q":
        print("saque realizado")
        break
    else:
        print("Favor digitar uma das opções acima")