import csv
import matplotlib.pyplot as plt
from simulations import limite_central as lc

def histograma(semente: int):
    tab_amostral = lc.get_resultados_amostrais(semente)
    tab_teorico = lc.get_resultados_teoricos()

    print(f"Media amostral: {tab_amostral['medias_amostrais']}")
    print(f"Desvio amostral: {tab_amostral['desvio_amostral']}")
    print(f"Media teorica: {tab_teorico['media_teorica']}")
    print(f"Desvio teorico: {tab_teorico['desvio_teorico']}")

    with open('tables/limite_central/resultados.csv', 'w') as ficheiro:
        writer = csv.writer(ficheiro)
        writer.writerow(['Media amostral', 'Desvio amostral', 'Media teorica', 'Desvio teorico'])
        writer.writerow([
            tab_amostral['medias_amostrais'], 
            tab_amostral['desvio_amostral'], 
            tab_teorico['media_teorica'], 
            tab_teorico['desvio_teorico']])

    plt.hist(tab_amostral['lista_medias'], bins = 20, density = True, alpha = 0.5, color = 'grey')
    plt.title('Distribuição das Médias Amostrais')
    plt.xlabel('Média Amostral')
    plt.ylabel('Frequências Relativas')
    plt.savefig("figures/limite_central/histograma_tcl.png", dpi=300)
    plt.show()