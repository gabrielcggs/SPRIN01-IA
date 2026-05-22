import os
import matplotlib.pyplot as plt


# Cria a pasta automaticamente
os.makedirs("output/graficos", exist_ok=True)


def gerar_grafico(dados):

    categorias = list(dados.keys())
    valores = list(dados.values())

    plt.figure(figsize=(8, 5))

    plt.bar(categorias, valores)

    plt.title("Resumo de Solicitações")

    plt.xlabel("Categorias")

    plt.ylabel("Quantidade")

    plt.savefig(
        "output/graficos/grafico.png"
    )

    plt.close()

    print("\nGráfico gerado com sucesso!")