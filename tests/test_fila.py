import pytest
from Model.Fila import Fila


def test_push_pop_len():
    f = Fila()
    f.push(1)
    f.push(2)
    assert len(f) == 2

    node = f.pop()
    # pop retorna um No (com atributo data)
    assert hasattr(node, 'data')
    assert node.data == 1
    assert len(f) == 1

    data = f.pop_inicio()
    assert data == 2
    assert len(f) == 0

    with pytest.raises(IndexError):
        f.pop()


def test_peek_and_eVazia_behaviour():
    f = Fila()
    assert f.eVazia() is True

    with pytest.raises(IndexError):
        f.peek()

    f.push(42)
    assert f.eVazia() is False
    node = f.peek()
    assert hasattr(node, 'data')
    assert node.data == 42
    # peek should not remove
    assert len(f) == 1

    # cleanup
    assert f.pop_inicio() == 42
