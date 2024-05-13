texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="") 
else:
    print()
    print("Executa no final do laço")

#exemplo com range
for numero in range(0, 51, 5):
    print(numero, end=" ")

#exemplo while 

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[3]Sair \n: " ))
    if opcao == 1:
        print("Sacando")
    elif opcao == 2:
        print("Exibindo o extrato")
    else:
        print("obrigado plea preferencia")

#exemplo break
while True:
    numero = int(input("Digite um numero: "))

    if numero == 10:
        break

    print(numero)