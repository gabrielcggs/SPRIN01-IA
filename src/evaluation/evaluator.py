import os
import matplotlib.pyplot as plt

os.makedirs("output/graficos", exist_ok=True)

def gerar_grafico():
    x = [1, 2, 3]
    y = [10, 20, 30]

    plt.plot(x, y)
    plt.savefig("output/graficos/grafico.png")
    plt.close()