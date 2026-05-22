import os


# Cria a pasta automaticamente
os.makedirs("output/reports", exist_ok=True)


def gerar_report(conteudo):

    caminho_arquivo = "output/reports/report.txt"

    with open(
        caminho_arquivo,
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(conteudo)

    print("\nRelatório gerado com sucesso!")