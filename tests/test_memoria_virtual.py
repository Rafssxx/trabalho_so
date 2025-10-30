from Model.MemoriaVirtual import MemoriaVirtual


def test_memoria_virtual_pages():
    mv = MemoriaVirtual(5)
    assert mv.tamanho_paginas == 5
    assert mv.paginas == [0, 1, 2, 3, 4]
