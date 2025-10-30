# Simulador de Gerenciamento de Memória com Paginação

Manual básico de execução (Windows)

## Requisitos

- Python 3.10+ instalado
- Recomenda-se usar o ambiente virtual do projeto `.venv`

## Preparação (PowerShell)

1. Criar o ambiente virtual (execute no diretório do projeto):

```powershell
python -m venv .venv
```

2. Ativar o venv (PowerShell):

```powershell
& ".\.venv\Scripts\Activate.ps1"
```

No Prompt de Comando (cmd.exe):

```cmd
.\.venv\Scripts\activate
```

3. Instalar dependências:

```powershell
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
```

## Executar a suíte de testes (pytest)

- Rodar todos os testes:

```powershell
& ".\.venv\Scripts\python.exe" -m pytest -q
```

- Rodar um arquivo de teste específico (exemplo):

```powershell
& ".\.venv\Scripts\python.exe" -m pytest tests\test_simulator_integration.py -q
```

## Executar o simulador

- Modo interativo (o programa pedirá entradas pelo prompt):

```powershell
& ".\.venv\Scripts\python.exe" main.py
```

- Modo não interativo (chamada direta da função `simular`):

```powershell
& ".\.venv\Scripts\python.exe" -c "from main import simular; simular(3,2,[0,1,0,2])"
```

## Estrutura principal do projeto

- `main.py` — interface e laço de simulação (função `simular`).
- `Model/MemoriaFisica.py` — lógica das molduras e política FIFO.
- `Model/Fila.py`, `Model/No.py` — implementação da fila encadeada.
- `Model/MemoriaVirtual.py` — definição do espaço de páginas.
- `tests/` — testes unitários e de integração (pytest).

## Dicas de solução de problemas

- Se receber `ImportError` ao rodar testes: confirme que está usando o Python do venv (`.venv\Scripts\python.exe`).
- Para depuração rápida, execute um único teste com o caminho do arquivo ou use `-k` para filtrar testes.
