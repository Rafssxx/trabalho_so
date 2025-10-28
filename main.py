from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm

from Model.MemoriaFisica import MemoriaFisica
from Model.MemoriaVirtual import MemoriaVirtual

console = Console()

def simular(input_paginas, input_molduras, acessos):
    memoria_virtual = MemoriaVirtual(input_paginas)
    memoria_fisica = MemoriaFisica(input_molduras)

    resultados = []
    falhas = 0

    fila_fifo = []  # fila para mostrar ordem FIFO

    for idx, acesso in enumerate(acessos, start=1):
        hit = False
        acao = ""

        # Verifica HIT
        atual = memoria_fisica.molduras.inicio
        while atual is not None:
            if acesso == atual.data:
                hit = True
                acao = "✅ HIT"
                break
            atual = atual.get_proximo()

        # MISS
        if not hit:
            falhas += 1
            # Se há espaço na memória física
            if memoria_fisica.get_tamanho_ocupado() < memoria_fisica.get_capacidade_total():
                memoria_fisica.molduras.push(acesso)
                fila_fifo.append(acesso)
                acao = f"❌ FALHA - Carrega P{acesso}"
            else:
                removido = memoria_fisica.molduras.pop_inicio()
                memoria_fisica.molduras.push(acesso)
                fila_fifo.pop(0)
                fila_fifo.append(acesso)
                acao = f"❌ FALHA - Substitui P{removido} por P{acesso}"

        # Captura estado da memória física
        memoria_atual = []
        atual = memoria_fisica.molduras.inicio
        while atual is not None:
            memoria_atual.append(str(atual.data))
            atual = atual.get_proximo()
        # Completa com '-' para visualização
        while len(memoria_atual) < input_molduras:
            memoria_atual.append('-')

        resultados.append({
            "passo": idx,
            "acesso": f"P{acesso}",
            "acao": acao,
            "falhas": str(falhas),
            "memoria": f"[{', '.join(memoria_atual)}]",
            "fila_fifo": f"[{', '.join(f'P{p}' for p in fila_fifo)}]"
        })

    # Impressão em tabela simples estilo didático
    console.print(f"{'Passo':<6} {'Acesso':<6} {'Ação':<30} {'Falhas':<6} {'Memória Física':<20} {'Fila FIFO':<20}")
    console.print('-'*90)
    for r in resultados:
        console.print(f"{r['passo']:<6} {r['acesso']:<6} {r['acao']:<30} {r['falhas']:<6} {r['memoria']:<20} {r['fila_fifo']:<20}")


def main():
    console.print("=== SIMULADOR DE GERENCIAMENTO DE MEMÓRIA ===")

    input_paginas = int(Prompt.ask("Digite o número de páginas da memória virtual"))
    input_molduras = int(Prompt.ask("Digite o número de molduras da memória física"))

    entrada = Prompt.ask("Lista de acessos (separados por vírgula)")
    acessos_lista = [int(x.strip()) for x in entrada.split(',') if x.strip() != ""]

    simular(input_paginas, input_molduras, acessos_lista)

if __name__ == "__main__":
    main()
