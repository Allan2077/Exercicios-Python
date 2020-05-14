#Entradas
vetor = []
soma = 0
#Processamento
for n in range(0, 20):
    num = int(input("Informe {0}/20 valor para o vetor: ".format(n+1)))
    vetor.append(num)
    soma = soma + num
print("Soma do vetor é {0}".format(soma))