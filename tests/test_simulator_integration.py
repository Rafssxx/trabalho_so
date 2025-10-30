import re
from Model.MemoriaFisica import MemoriaFisica
from Model.MemoriaVirtual import MemoriaVirtual
from main import simular


def test_simular_outputs_expected(capsys):
    # Cenário simples: 3 páginas (0..2), 2 molduras, acessos com hits e falhas
    acessos = [0, 1, 0, 2]
    simular(3, 2, acessos)

    captured = capsys.readouterr()
    out = captured.out

    # Deve conter Passo e Acesso (P0, P1, ...)
    assert "Passo" in out
    assert "Acesso" in out
    # Verifica ocorrência de P0 e marcações de FALHA/HIT
    assert re.search(r"P0", out)
    assert ("FALHA" in out) or ("HIT" in out)
