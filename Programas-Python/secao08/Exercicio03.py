#Entradas
vetor = []
for n in range (0, 10):
    num = int(input("Digite um valor: "))
    vetor.append(num)
    #Processamento
vetor.reverse()#reverte a lista
for n in vetor:
    print(n)