#Entradas
valor_por_horas = float(input("Informe o valor por horas: "))
horas_trabalhadas = float(input("Horas trabalhas : "))
#Processamento
Salario = (horas_trabalhadas * valor_por_horas)
#Saída
print("O salario é de R${0:.2f}".format(Salario))
                