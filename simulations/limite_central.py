import numpy as np

def get_medias(teste_amostral: int, teste_replicacoes: int, lam: float, semente: int):
    media_teorica = 1 / lam
    np.random.seed(semente)
    sorteio = np.random.exponential(media_teorica, size=(teste_replicacoes, teste_amostral))
    medias = np.mean(sorteio, axis=1)
    medias_amostrais = np.mean(medias)

    return {
        'medias_amostrais': medias_amostrais,
        'media_teorica': media_teorica,
        'medias': medias
    }

def get_eixos(media_teorica: float, teste_amostral: int):
    desvio_padrao_teorico = media_teorica / np.sqrt(teste_amostral)
    esquerda = media_teorica - 4 * desvio_padrao_teorico
    direita = media_teorica + 4 * desvio_padrao_teorico
    x = np.linspace(esquerda, direita, 500)
    normal = (1 / (desvio_padrao_teorico * np.sqrt(2 * np.pi))) * np.exp(-(x - media_teorica) ** 2 / (2 * desvio_padrao_teorico ** 2))

    return x, normal