import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from simulations import passeio_aleatorio as pads
from IPython.display import display


sns.set_theme(style='whitegrid')
paleta = {
    'Analítica': plt.cm.tab10(0),
    'Empírica': plt.cm.tab10(1)
}

def formatar_e_salvar(ax, titulo: str, xlabel: str, ylabel: str, caminho: str):
    ax.set_title(titulo, pad=15, weight='bold')
    ax.set_xlabel(xlabel, labelpad=15)
    ax.set_ylabel(ylabel, labelpad=15)
    plt.tight_layout()
    plt.savefig(caminho, dpi=300)
    plt.show()

def exportar_csv(nome_arq: str, N: list, M: list, pa: list, pe: list):
    tabela = pd.DataFrame({
        'Passos': N,
        'Replicações': M,
        'Probabilidade Analítica': pa,
        'Probabilidade Empírica': pe
    })
    tabela.index = range(1, len(tabela) + 1)
    path = f'tables/passeio-aleatorio/{nome_arq}.csv'
    tabela.to_csv(path, index=False, encoding='utf-8')
    return tabela

def passeio_empirico(N: int):
    _, ax = plt.subplots(figsize=(10,6))
    trajeto, _ = pads.get_passeio_aleatorio(N)
    print(f'Gráfico de um passeio aleatório unidimensional simétrico com N = {N} passos.')
    ax.plot(trajeto, color=paleta['Empírica'])
    ax.axhline(0, color='black', linestyle='--', linewidth=1.5)
    formatar_e_salvar(
        ax,
        f'Passeio com {N} passos',
        'Passo',
        'Posição',
        'figures/passeio-aleatorio/passeio.png'
    )

def trajetorias_empiricas(N: int):
    _, ax = plt.subplots(figsize=(10,6))
    print(f'Gráfico com 10 exemplos de PADS com N = {N} passos.')
    for _ in range(10):
        trajeto, _ = pads.get_passeio_aleatorio(N)
        ax.plot(trajeto)
    ax.axhline(0, color='black', linestyle='--', linewidth=1.5)
    formatar_e_salvar(
        ax,
        f'10 Passeios com {N} Passos',
        'Passo',
        'Posição',
        'figures/passeio-aleatorio/trajetorias.png'
    )

def convergencia_monte_carlo(N: int, M: int):
    pa = pads.get_analitica(N)
    pe = pads.get_empirica(N, M)

    print(f"Probabilidade Analítica com {N} passos : {pa:.4f}")
    print(f"Probabilidade Empírica com {N} passos em {M} replicações: {pe:.4f}")
    print()

    x,y = pads.get_eixos_carlo(N)
    print(
        'Gráfico e tabela da convergência das probabilidades'
        f'\ncom N = {N} fixo e M variando em {x}.'
    )
    _, ax = plt.subplots(figsize=(10,6))
    ax.axhline(
        pa,
        color=paleta['Analítica'],
        linewidth=1.5,
        label='Analítica'
    )
    ax.plot(
        x,
        y,
        marker='o',
        color=paleta['Empírica'],
        linestyle='--',
        label='Empírica'
    )

    ax.set_xscale('log')
    ax.legend()
    formatar_e_salvar(
        ax,
        f'Convergência de Monte Carlo (N = {N} fixo)',
        'Número de Simulações (M) - Escala Log',
        'Probabilidade de Retorno à Origem',
        'figures/passeio-aleatorio/convergencia_M.png'
    )

    tabela = exportar_csv(
        'convergencia-carlo',
        N=[N] * len(pads.SCALE),
        M=x,
        pa=[round(pa, 4)] * len(pads.SCALE),
        pe=np.round(y, 4)
    )
    display(tabela)

def convergencia_stirling(M: int):
    x, ya, ye = pads.get_eixos_stirling(M)

    _, ax = plt.subplots(figsize=(10,6))
    print(
        'Gráfico e tabela do limite das probabilidades'
        f'\ncom M = {M} fixo e N variando em {x}.'
    )
    ax.plot(x, ya, marker='s', color=paleta['Analítica'], label='Analítica')
    ax.plot(x, ye, marker='o', color=paleta['Empírica'], linestyle='--', label='Empírica')
    ax.axhline(
        0,
        color='black',
        linestyle='--',
        linewidth=1,
    )

    ax.set_xscale('log')
    ax.legend()
    formatar_e_salvar(
        ax,
        f'Limite das Probabilidades com N Crescente e M={M} fixo',
        'Número de Passos (N) - Escala Log',
        'Probabilidade de Retorno à Origem',
        'figures/passeio-aleatorio/convergencia_S.png'
    )

    tabela = exportar_csv(
        'convergencia-stirling',
        N=x,
        M=[M] * len(pads.SCALE),
        pa=np.round(ya, 4),
        pe=np.round(ye, 4)
    )
    display(tabela)