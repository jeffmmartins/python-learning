nome = "Jefferson"
idade = 35
profissao = "programador"
linguagem = "Python"
saldo = 45.7777

dados = {"nome": "guilherme", "idade": 35}

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(nome, idade))
print("Nome: {name} Idade: {age} Nome: {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade} Nome: {idade} {nome}".format(**dados))
print(f"nome: {nome} idade: {idade} saldo: {saldo:10.2f}")