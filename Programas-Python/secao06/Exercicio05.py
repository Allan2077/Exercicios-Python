#Entradas
peso = float(input("Informe o peso: "))
#Processamento
if peso > 50:
    m = (peso - 50) * 4.00
    e = 'excesso'
    print("A multa a pagar é de {0:.2f}".format(m))
else:
    e = peso < 50
    print("Não há excesso".format(e))