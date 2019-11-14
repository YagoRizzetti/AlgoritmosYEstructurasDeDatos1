__author__ = 'Cátedra de AED'


def ackermann(m, n):
    """Funcion de Ackermann.

    Calcula y retorna el valor de la funcion de Ackermann
    para los numeros m y n que se suponen enteros no negativos.

    :param m: el primer valor para el calculo (m entero, m >=0)
    :param n: el segundo valor para el calculo (n entero, n >=0)
    :return: el valor de la funcion de Ackermann.
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

