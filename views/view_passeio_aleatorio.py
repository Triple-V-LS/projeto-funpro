import matplotlib.pyplot as plt
import seaborn as sns
from simulations import passeio_aleatorio as pads


sns.set_theme(style='whitegrid')
paleta = {
    'Analítica': plt.cm.tab10(0),
    'Empírica': plt.cm.tab10(1)
}

def passeio_empirico(N: int):
    _, ax = plt.subplots(figsize=(10,6))
    trajeto, _ = pads.get_passeio_aleatorio(N)
    print(f'Gráfico de um passeio aleatório unidimensional simétrico com N = {N} passos.')
    ax.plot(trajeto, color=paleta['Empírica'])
    ax.set_title(f'Exemplo de PADS com N={N}', pad=15, weight='bold')
    ax.set_xlabel('Passo', labelpad=15)
    ax.set_ylabel('Posição', labelpad=15)
    ax.axhline(0, color='black', linestyle='--', linewidth=1.5)

    plt.tight_layout()
    plt.savefig('figures/passeio-aleatorio/passeio.png',dpi=300)
    plt.show()

def trajetorias_empiricas(N: int):
    _, ax = plt.subplots(figsize=(10,6))
    print(f'Gráfico com 10 exemplos de PADS com N = {N} passos.')
    for _ in range(10):
        trajeto, _ = pads.get_passeio_aleatorio(N)
        ax.plot(trajeto)
    ax.set_title(f'10 Trajétorias com {N} Passos', pad=15, weight='bold')
    ax.set_xlabel('Passo', labelpad=15)
    ax.set_ylabel('Posição', labelpad=15)
    ax.axhline(0, color='black', linestyle='--', linewidth=1.5)

    plt.tight_layout()
    plt.savefig('figures/passeio-aleatorio/trajetorias.png',dpi=300)
    plt.show()


def convergencia_monte_carlo(N: int, M: int):
    pa = pads.get_analitica(N)
    pe = pads.get_monte_carlo(N, M)

    print(f"Probabilidade Analítica com {N} passos : {pa:.4f}")
    print(f"Probabilidade Empírica com {N} passos em {M} simulações: {pe:.4f}")
    print()

    x,y = pads.get_eixos_convM(N, M)
    print(
        'Gráfico da convergência das probabilidades analítica e empírica'
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
    ax.set_title(f'Convergência de Monte Carlo (N = {N} fixo)', pad=15, weight='bold')
    ax.set_xlabel('Número de Simulações (M) - Escala Log', labelpad=15)
    ax.set_ylabel('Probabilidade de Retorno à Origem', labelpad=15)
    ax.legend()

    plt.tight_layout()
    plt.savefig('figures/passeio-aleatorio/convergencia_M.png',dpi=300)
    plt.show()


def convergencia_stirling(M: int):
    x, ya, ye = pads.get_eixos_convS(M)

    _, ax = plt.subplots(figsize=(10,6))
    print(
        'Gráfico do limite das probabilidades analítica e empírica'
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
    ax.set_title(f'Limite das Probabilidades com N Crescente e M={M} fixo', pad=15, weight='bold')
    ax.set_xlabel('Número de Passos (N) - Escala Log', labelpad=15)
    ax.set_ylabel('Probabilidade de Retorno à Origem', labelpad=15)
    ax.legend()

    plt.tight_layout()
    plt.savefig('figures/passeio-aleatorio/convergencia_S.png', dpi=300)
    plt.show()