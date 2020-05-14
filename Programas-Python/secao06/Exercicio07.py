#Variaveis
n1 = int(input("Informe um numero "))
n2 = int(input("Informe um numero "))
n3 = int(input("Informe um numero "))
n4 = int(input("Informe um numero "))
#Entradas

q1 = n1 * n1
q2 = n2 * n2
q3 = n3 * n3
q4 = n4 * n4
#Processamento

if q3 >= 1000:
    print(q3)
else:
    print("n1: {0}, Quadrado: {1}".format(n1, q1))
    print("n2: {0}, Quadrado: {1}".format(n2, q2))
    print("n3: {0}, Quadrado: {1}".format(n3, q3))
    print("n4: {0}, Quadrado: {1}".format(n4, q4))