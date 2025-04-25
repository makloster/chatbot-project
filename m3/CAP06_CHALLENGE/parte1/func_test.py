import pytest

from func import es_primo


# Números primos conocidos
@pytest.mark.parametrize("num", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
def test_numeros_primos(num):
    assert es_primo(num) is True


# Números no primos conocidos
@pytest.mark.parametrize("num", [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20])
def test_numeros_no_primos(num):
    assert es_primo(num) is False


# Números negativos
@pytest.mark.parametrize("num", [-1, -2, -3, -5, -11, -13])
def test_numeros_negativos(num):
    assert es_primo(num) is False


# Números grandes
def test_primo_grande():
    assert es_primo(1000003) is True


def test_no_primo_grande():
    assert es_primo(1000004) is False


# Tipos no enteros - deben lanzar TypeError
@pytest.mark.parametrize(
    "valor", [2.3, 3.9, "tres", None, True, False, "cinco", [], {}]
)
def test_valores_no_enteros(valor):
    with pytest.raises(TypeError):
        es_primo(valor)


# Precision en punto flotante cerca de enteros primos
@pytest.mark.parametrize("num", [19.000000000000004, 23.000000000000004])
def test_flotantes_cercanos_a_primos(num):
    assert es_primo(num) is True
