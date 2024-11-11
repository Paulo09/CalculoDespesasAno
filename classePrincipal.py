# Classe de Instancia Principal - Classe de Instancia Despesas x ano
#@PauloCaatro

def main():
    arquivo = 'despesas.csv'  # Substitua pelo nome do seu arquivo
    despesas = carregar_dados(arquivo)

    while True:
        ano = int(input("Digite o ano para calcular o total das despesas (0 para sair): "))
        if ano == 0:
            break
        total = calcular_total_por_ano(despesas, ano)
        if total > 0:
            print(f"O valor total das despesas em {ano} foi: R$ {total:.2f}")
        else:
            print(f"Não foram encontradas despesas para o ano {ano}.")

if __name__ == "__main__":
    main()