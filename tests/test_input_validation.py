import pytest
from main import validar_inputs


def test_validar_inputs_accepts_valid_data():
    # Não deve levantar exceção
    validar_inputs(3, 2, [0, 1, 2])


def test_validar_inputs_rejects_non_positive():
    with pytest.raises(ValueError):
        validar_inputs(0, 2, [0])
    with pytest.raises(ValueError):
        validar_inputs(3, 0, [0])


def test_validar_inputs_rejects_empty_acessos():
    with pytest.raises(ValueError):
        validar_inputs(3, 2, [])


def test_validar_inputs_rejects_invalid_acessos():
    # negativos ou fora do intervalo
    with pytest.raises(ValueError):
        validar_inputs(3, 2, [-1, 0])
    with pytest.raises(ValueError):
        validar_inputs(3, 2, [0, 3])


def test_validar_inputs_rejects_non_integer_inputs():
    with pytest.raises(ValueError):
        validar_inputs('3', 2, [0])
    with pytest.raises(ValueError):
        validar_inputs(3, '2', [0])
    with pytest.raises(ValueError):
        validar_inputs(3, 2, [0, '1'])
