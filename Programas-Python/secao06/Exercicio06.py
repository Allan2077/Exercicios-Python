#Entradas
valor_hora = 10.00
valor_hora_excedente = 20.00
e = 0

codigo = int(input("Informe o codigo: "))
horas_trabalhadas= int(input("Informe a quantidade de horas trabalhadas: ")) 
#Processamento
if horas_trabalhadas > 50:
    e = (horas_trabalhadas - 50) * valor_hora_excedente #20.00
    salario = (50 * valor_hora) + e # 10.00
    print("Seu salario é de {0:.2f}".format(salario))
    print("O valor em horas extra é de {0:.2f}".format(e))     
else:
    salario = (horas_trabalhadas * valor_hora)#10.00
    print("Seu salario é de {0:.2f}".format(salario))
    print("O valor em horas extra é de {0:.2f}".format(e))