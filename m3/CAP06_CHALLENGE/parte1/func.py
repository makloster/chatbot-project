def es_primo(num):
    if isinstance(num, bool):
        raise TypeError("El valor no puede ser booleano.")

    if not isinstance(num, (int, float)):
        raise TypeError("El valor debe ser un número entero.")

    if isinstance(num, float):
        if abs(num - round(num)) < 1e-9:
            num = round(num)
        else:
            raise TypeError("El valor debe ser un entero exacto.")

    num = int(num)  # Convertimos explícitamente a entero después de validarlo

    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True


if __name__ == "__main__":
    print(es_primo(5))
