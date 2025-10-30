import pytest
from Model.MemoriaFisica import MemoriaFisica


def test_inserir_contem_listar_substituir():
    mf = MemoriaFisica(2)
    assert mf.get_capacidade_total() == 2
    assert mf.get_tamanho_ocupado() == 0

    assert mf.inserir(10) is True
    assert mf.inserir(20) is True
    # inserir quando cheia retorna False
    assert mf.inserir(30) is False

    assert mf.contem(10)
    assert mf.contem(20)
    assert not mf.contem(30)

    assert mf.listar_molduras() == [10, 20]

    removed = mf.substituir_fifo(30)
    assert removed == 10
    assert mf.listar_molduras() == [20, 30]


def test_capacidade_zero_substituicao_gera_erro():
    mf = MemoriaFisica(0)
    assert mf.get_capacidade_total() == 0
    # inserir quando capacidade 0 devolve False
    assert mf.inserir(1) is False

    # substituir_fifo deve propagar erro por pop_inicio em fila vazia
    with pytest.raises(IndexError):
        mf.substituir_fifo(5)


def test_duplicatas_e_substituicao_com_uma_moldura():
    mf = MemoriaFisica(3)
    # inserir duplicatas é permitido
    assert mf.inserir(7) is True
    assert mf.inserir(7) is True
    assert mf.listar_molduras() == [7, 7]

    # testar substituição com apenas 1 moldura
    mf1 = MemoriaFisica(1)
    assert mf1.inserir(9) is True
    assert mf1.listar_molduras() == [9]
    removed = mf1.substituir_fifo(10)
    assert removed == 9
    assert mf1.listar_molduras() == [10]
