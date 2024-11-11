
# Carregar Dados
#@PauloCastro
import csv

def carregar_dados(arquivo):
    despesas = []
    with open(arquivo, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Pula a primeira linha (cabeçalho)
        next(reader)
        for row in reader:
            ano, mes, despesa, valor = row
            despesas.append(Despesa(int(ano), mes, despesa, float(valor)))
    return despesas
