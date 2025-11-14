def somar(a,b):
    return a + b

def comprimento(lista):
    return len(lista)

def test_somar():
    assert somar(2,3) == 5
    assert somar(3,5) == 8

def comprimento():
    assert comprimento({1,2,3,6,8,9}) == 4
    assert comprimento({1,2,3,4,5}) == 5