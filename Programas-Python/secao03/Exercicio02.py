#entradas
quantidade_minima = int(input("Informe a quantidade minima: "))
quantidade_maxima = int(input("Informe a quantidade maxima: "))
#processamento
estoque_medio = (quantidade_maxima + quantidade_minima) / 2
#saida
print("O estoque médio é {0}".format(estoque_medio))