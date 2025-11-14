from funcoes import *


def test_email_valido():
    assert email_valido("senna.j@senai.com.nr") is True
    assert email_valido("senaldoj.senai.com.nr") is False


def test_dividir():
    assert dividir(4,2) == 2
    assert dividir(4,0) is None

