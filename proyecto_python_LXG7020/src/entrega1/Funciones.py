import math
from datetime import date
from datetime import date

def es_fecha_valida(dia: int, mes: int, año: int) -> bool:
    try:
        # Verifica si la fecha existe
        fecha = date(año, mes, dia)

        # Verifica si el año es bisiesto
        bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

        # Ajuste para Zeller
        if mes < 3:
            mes += 12
            año -= 1

        K = año % 100
        J = año // 100

        h = (dia + (13 * (mes + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

        # h = 0 es sábado, h = 1 es domingo, h = 2 es lunes, ..., h = 6 es viernes
        return h != 1

    except ValueError:
        return False


def producto(n: int, k: int) -> int:
    """
    Calcula el producto descendente de n en k términos: n \* (n-1) \* ... \* (n-k+1).

    Parámetros:
        n (int): Número inicial, debe ser mayor que k.
        k (int): Cantidad de términos a multiplicar.

    Retorna:
        int: Resultado del producto descendente.

    Lanza:
        AssertionError: Si n no es mayor que k.
    """
    assert n > k, "n debe ser mayor o igual a k"
    p = 1
    for i in range(0, k):
        p *= (n - i + 1)
    return p

def secuencia_geom(a1: float, r: float, k: int) -> float:
    """
    Calcula el k-ésimo término de una secuencia geométrica especial.

    Parámetros:
        a1 (float): Primer término de la secuencia.
        r (float): Razón de la secuencia.
        k (int): Índice del término a calcular (debe ser >= 1).

    Retorna:
        float: Valor del k-ésimo término.

    Lanza:
        ValueError: Si k es menor que 1.
    """
    if k < 1:
        raise ValueError("k debe ser mayor o igual a 1")
    return (a1 ** k) * (r ** ((k * (k - 1)) // 2))

def combinatorio(n: int, k: int) -> int:
    """
    Calcula el coeficiente binomial (n sobre k).

    Parámetros:
        n (int): Número total de elementos.
        k (int): Número de elementos a elegir.

    Retorna:
        int: Valor del coeficiente binomial.

    Lanza:
        AssertionError: Si n es menor que k.
    """
    assert n >= k, "n debe ser mayor o igual a k"
    return math.comb(n, k)

def SNK(n: int, k: int) -> float:
    """
    Calcula el número de Stirling de segunda especie S(n, k).

    Parámetros:
        n (int): Número de elementos.
        k (int): Número de subconjuntos.

    Retorna:
        float: Número de particiones posibles.

    Lanza:
        AssertionError: Si n es menor que k.
    """
    assert n >= k, "n debe ser mayor o igual a k"
    suma = 0
    for i in range(0, k):
        signo = (-1) ** i
        numerador = k + 1
        denominador = i + 1
        potencia = (k - i) ** n
        termino = signo * combinatorio(numerador, denominador) * potencia
        suma += termino

    return (1 / math.factorial(k)) * suma
