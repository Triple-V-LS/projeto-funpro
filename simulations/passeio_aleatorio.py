import numpy as np
import math

SCALE = [10, 50, 100, 500, 1000, 5000, 10_000, 50_000, 100_000]

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

def get_empirica(N: int, M: int):
    qtd_sucessos = 0
    for _ in range(M):
        _, retornou_origem = get_passeio_aleatorio(N)
        if retornou_origem:
            qtd_sucessos += 1
    pe = qtd_sucessos / M
    return pe

##################################################

def get_eixos_carlo(N: int):
    def empiricas(N:int, qtd_replicacoes: list[int]):
        empiricas = []
        for m in qtd_replicacoes:
            pe = get_empirica(N, m)
            empiricas.append(pe)
        return empiricas
    
    replicacoes = SCALE
    return replicacoes, empiricas(N, replicacoes)

def get_eixos_stirling(M: int):
    passos = SCALE
    analiticas = []
    empiricas = []

    for n in passos:
        pa = get_analitica(n) 
        pe = get_empirica(n, M)
        analiticas.append(pa)
        empiricas.append(pe)

    return passos, analiticas, empiricas