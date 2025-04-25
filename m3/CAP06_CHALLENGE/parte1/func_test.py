import pytest

from func import es_primo


# Verifica que la función identifica correctamente los números primos conocidos.
# Esto es importante porque la detección de números primos es el propósito principal de la función.
@pytest.mark.parametrize("num", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
def test_numeros_primos(num):
    assert es_primo(num) is True


# Verifica que la función identifica correctamente los números que no son primos.
# Es crucial probar estos casos para asegurar que la función no da falsos positivos,
# especialmente con casos especiales como 0 y 1 que no son primos por definición.
@pytest.mark.parametrize("num", [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20])
def test_numeros_no_primos(num):
    assert es_primo(num) is False


# Verifica que la función maneja correctamente los números negativos.
# Por definición matemática, los números negativos no son primos, por lo que
# la función debe devolver False para cualquier entrada negativa.
@pytest.mark.parametrize("num", [-1, -2, -3, -5, -11, -13])
def test_numeros_negativos(num):
    assert es_primo(num) is False


# Verifica que la función puede identificar correctamente un número primo grande.
# Esta prueba es importante para evaluar el rendimiento y la precisión de la función
# con números que podrían causar problemas de eficiencia o desbordamiento.
def test_primo_grande():
    assert es_primo(1000003) is True


# Verifica que la función puede identificar correctamente un número grande que no es primo.
# Complementa la prueba anterior para asegurar que la función mantiene su precisión
# con números grandes que no son primos.
def test_no_primo_grande():
    assert es_primo(1000004) is False


# Verifica que la función lanza TypeError cuando se le pasan valores que no son enteros.
# Es importante validar las entradas para evitar comportamientos inesperados y
# proporcionar mensajes de error claros cuando los tipos de datos son incorrectos.
@pytest.mark.parametrize(
    "valor", [2.3, 3.9, "tres", None, True, False, "cinco", [], {}]
)
def test_valores_no_enteros(valor):
    with pytest.raises(TypeError):
        es_primo(valor)


# Verifica que la función maneja correctamente números de punto flotante que están muy cerca de enteros primos.
# Debido a la imprecisión inherente de los números de punto flotante en computación,
# es importante probar cómo la función maneja valores que son casi enteros.
@pytest.mark.parametrize("num", [19.000000000000004, 23.000000000000004])
def test_flotantes_cercanos_a_primos(num):
    assert es_primo(num) is True
