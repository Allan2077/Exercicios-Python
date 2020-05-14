#Entradas
indice = float(input("Informe o índice de poluição: "))
#Processamento
if (indice >= 0.3 and indice <0.4):
    print("Grupo 1 suspender atividades")
elif (indice >= 0.4 and indice < 0.5):
        print("Grupo 1 e 2 suspendam as atividades")
elif(indice >= 0.5):
            print("Todos os grupos suspendam atividades")
