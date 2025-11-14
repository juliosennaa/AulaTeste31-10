import pytest

@pytest.fixture(scope="function")
def fixure_function():
    return 10

@pytest.fixture(scope="modelo")
def fixure_module():
    return 20

@pytest.fixture(scope="session")
def fixure_session():
    return 40

def test_1(fixure_function):
    assert fixure_function == 10


def test_2(fixure_function, fixure_module):
    assert fixure_function == 10
    assert fixure_module == 20
    
def test_3(fixure_function, fixure_session):
    assert fixure_function == 10
    assert fixure_session == 40

    
    

