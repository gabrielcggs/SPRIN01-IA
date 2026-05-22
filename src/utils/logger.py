import os
from datetime import datetime


# Cria a pasta automaticamente
os.makedirs("output/logs", exist_ok=True)


def salvar_log(texto):

    caminho_arquivo = "output/logs/log.txt"

    with open(
        caminho_arquivo,
        "a",
        encoding="utf-8"
    ) as arquivo:

        horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        arquivo.write(
            f"[{horario}] {texto}\n"
        )