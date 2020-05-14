#Entrada
altura = float(input("Informe a altura: "))
sexo = input("Informe o sexo: ")
#Processamento
if  sexo.lower() == "m":     #.lower ele entende a letra maiúscula ou minúscula
    peso_ideal = (72.7 * altura) - 58
elif  sexo.lower() == "f":
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
    print("Sexo indefinido")
    
print("peso ideal é = {0:.2f}".format(peso_ideal))
    