#Entrada
maior = 0
numero = int(input("Informe um número: "))
#Processamento
while numero != 0:
    if numero > maior:
        maior = numero
    numero = int(input("Informe um número: "))
print("Maior valor {0}".format(maior))