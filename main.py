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

    # Itera acessos usando a interface de MemoriaFisica (encapsulada)
    for idx, acesso in enumerate(acessos, start=1):
        acao = ""

        # Verifica HIT usando método encapsulado
        if memoria_fisica.contem(acesso):
            acao = "✅ HIT"
        else:
            # MISS
            falhas += 1
            # Se há espaço na memória física
            if memoria_fisica.get_tamanho_ocupado() < memoria_fisica.get_capacidade_total():
                memoria_fisica.inserir(acesso)
                acao = f"❌ FALHA - Carrega P{acesso}"
            else:
                removido = memoria_fisica.substituir_fifo(acesso)
                acao = f"❌ FALHA - Substitui P{removido} por P{acesso}"

        # Captura estado da memória física (lista em ordem FIFO)
        memoria_atual = [str(x) for x in memoria_fisica.listar_molduras()]
        # Completa com '-' para visualização
        while len(memoria_atual) < input_molduras:
            memoria_atual.append('-')

        fila_fifo_exibicao = [f"P{p}" for p in memoria_fisica.listar_molduras()]

        resultados.append({
            "passo": idx,
            "acesso": f"P{acesso}",
            "acao": acao,
            "falhas": str(falhas),
            "memoria": f"[{', '.join(memoria_atual)}]",
            "fila_fifo": f"[{', '.join(fila_fifo_exibicao)}]"
        })

    # Impressão usando rich.Table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Passo", justify="right")
    table.add_column("Acesso", justify="center")
    table.add_column("Ação", justify="left")
    table.add_column("Falhas", justify="right")
    table.add_column("Memória Física", justify="left")
    table.add_column("Fila FIFO", justify="left")

    for r in resultados:
        table.add_row(str(r['passo']), r['acesso'], r['acao'], r['falhas'], r['memoria'], r['fila_fifo'])

    console.print(table)


def main():
    console.print("=== SIMULADOR DE GERENCIAMENTO DE MEMÓRIA ===")

    # Leitura e validação de entradas
    try:
        input_paginas = int(Prompt.ask("Digite o número de páginas da memória virtual"))
        input_molduras = int(Prompt.ask("Digite o número de molduras da memória física"))
    except ValueError:
        console.print("[red]Entradas inválidas: informe números inteiros.[/red]")
        return

    if input_paginas <= 0 or input_molduras <= 0:
        console.print("[red]O número de páginas e molduras deve ser maior que zero.[/red]")
        return

    entrada = Prompt.ask("Lista de acessos (separados por vírgula)")
    try:
        acessos_lista = [int(x.strip()) for x in entrada.split(',') if x.strip() != ""]
    except ValueError:
        console.print("[red]A lista de acessos deve conter apenas números inteiros separados por vírgula.[/red]")
        return

    if len(acessos_lista) == 0:
        console.print("[red]Nenhum acesso informado.[/red]")
        return

    # Valida se acessos estão dentro do intervalo de páginas válidas
    invalidos = [a for a in acessos_lista if a < 0 or a >= input_paginas]
    if invalidos:
        console.print(f"[red]Acessos inválidos (fora do intervalo 0..{input_paginas-1}): {invalidos}[/red]")
        return

    simular(input_paginas, input_molduras, acessos_lista)

if __name__ == "__main__":
    main()
