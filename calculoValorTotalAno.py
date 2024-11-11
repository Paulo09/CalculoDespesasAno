# Classe Responsavel pelo calculo Total parametro Ano x Despesa
#@PauloCastro

def calcular_total_por_ano(despesas, ano):
    total = 0
    for despesa in despesas:
        if despesa.ano == ano:
            total += despesa.valor
    return total
