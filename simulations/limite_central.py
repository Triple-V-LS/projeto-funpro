import numpy as np

TESTE_AMOSTRAL = 100
TESTE_REPLICACOES = 10_000

def get_resultados_amostrais(semente: int):
    np.random.seed(semente)
    sorteio = np.random.randint(140, 251, size = (TESTE_REPLICACOES, TESTE_AMOSTRAL))
    print(sorteio.shape)

    lista_medias = np.mean(sorteio, axis = 1)
    medias_amostrais = np.mean(lista_medias)
    desvio_amostral = np.std(lista_medias)

    return {
        'lista_medias': lista_medias,
        'medias_amostrais': medias_amostrais,
        'desvio_amostral': desvio_amostral
    }

def get_resultados_teoricos():
    media_teorica = (140 + 250) / 2
    desvio_teorico = np.sqrt((((250 - 140 + 1) ** 2 - 1) / 12) / TESTE_AMOSTRAL)
    return {
        'media_teorica': media_teorica,
        'desvio_teorico': desvio_teorico
    }
