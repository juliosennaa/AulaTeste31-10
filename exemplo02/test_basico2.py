def e_positivo(numero):
    return numero > 0


def test_epositivo():
    assert e_positivo(5) == True
    assert e_positivo(-5) == False
