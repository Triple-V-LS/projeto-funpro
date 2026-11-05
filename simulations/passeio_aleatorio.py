import numpy as np
import math

def get_passeio_aleatorio(N: int):
    passos = np.random.choice([-1,1], size=N)
    trajeto = np.insert(
        arr= np.cumsum(passos),
        obj=0,
        values=0
    )
    return trajeto, trajeto[N] == 0

def get_analitica(N):
    if N % 2 != 0:
        return 0.0
    return math.comb(N, N // 2) / (2 ** N)

def get_monte_carlo(N: int, M: int):
    qtd_sucessos = 0
    for _ in range(M):
        _, retornou_origem = get_passeio_aleatorio(N)
        if retornou_origem:
            qtd_sucessos += 1
    p_empirica = qtd_sucessos / M
    return p_empirica

##################################################

def get_eixos_convM(N: int, M: int):
    def empiricas(N:int, qtd_replicacoes: list[int]):
        empiricas = []
        for m in qtd_replicacoes:
            p = get_monte_carlo(N, m)
            empiricas.append(p)
        return empiricas
    
    replicacoes = [10, 50, 100, 500, 1000, 5000, 10_000, 50_000, 100_000]
    return replicacoes, empiricas(N, replicacoes)

def get_eixos_convS(M: int):
    passos = [10, 50, 100, 500, 1000, 5000, 10_000, 50_000, 100_000]
    analiticas = []
    empiricas = []

    for n in passos:
        pa = get_analitica(n) 
        pe = get_monte_carlo(n, M)
        analiticas.append(pa)
        empiricas.append(pe)

    return passos, analiticas, empiricas