import csv
import matplotlib.pyplot as plt
from simulations import limite_central as lc

def histograma(teste_amostral: int, teste_replicacoes: int, lam: float, semente: int):
    tab_medias = lc.get_medias(teste_amostral, teste_replicacoes, lam, semente)
    medias_amostrais = tab_medias['medias_amostrais']
    media_teorica = tab_medias['media_teorica']
    medias = tab_medias['medias']

    x, normal = lc.get_eixos(media_teorica, teste_amostral)

    print(f"Media amostral: {medias_amostrais}")
    print(f"Media teórica: {media_teorica}")

    with open('tables/limite_central/resultados.csv', 'w') as ficheiro:
        anota = csv.writer(ficheiro)
        anota.writerow(['Media amostral', 'Media teórica'])
        anota.writerow([medias_amostrais, media_teorica])

    _, ax = plt.subplots(figsize=(8, 6))
    ax.hist(medias, bins=20, density=True, rwidth=0.85, alpha=0.5, color="blue", label="empírico")
    ax.plot(x, normal, color="tab:red", linewidth=2, label="teórico")
    ax.set_title('Distribuição das Médias Amostrais')
    ax.set_xlabel('Média Amostral')
    ax.set_ylabel('Densidade de Probabilidade')
    ax.legend()
    plt.savefig("figures/limite_central/histograma_tcl.png", dpi=300)
    plt.show()