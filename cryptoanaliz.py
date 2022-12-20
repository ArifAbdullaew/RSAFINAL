import sympy


def rsa_key_find(e, n):
    # Находим простые множители числа n
    factors = sympy.factorint(n)

    # Находим phi
    phi = 1
    for p in factors:
        phi *= (p - 1)

        # Находим закрытый ключ
    d = sympy.mod_inverse(e, phi)

    # Возвращаем открытый и закрытый ключи
    return ((e, n), (d, n))


# Пример
e = 5
n = 91

print("RSA Keys:", rsa_key_find(e, n))
