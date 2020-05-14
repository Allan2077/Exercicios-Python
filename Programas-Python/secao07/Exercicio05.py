#Variaveis
nome = input("Informe o nome: ")
senha = input("Informe a senha: ")
#Processamento
while nome == senha:
    print("Senha não pode ser igual nome!")
    nome = input("Informe o nome: ")
    senha = input("Informe a senha: ")
    