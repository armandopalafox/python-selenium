from unittest import result


def es_par(a, b):
    if a % 2 == 0 and b % 2 ==0:
        return True
    else:
        return False

def test_positive():
    result = es_par(2, 4)
    assert result == True, "Los numeros no son pares"

    # if result == True:
    #     pass
    # else:
    #     print("Los numeros no son pares")

def test_negative():
    result = es_par(3, 9)
    assert not result

def test_decimal():
    result = es_par(1.99999999999999999999, 2.00000000000000000001)
    assert result