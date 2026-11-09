from Calculadora import fatorial

def test_fatorial_de_5():
    assert fatorial(5) == 120

def test_fatorial_de_zero():
    assert fatorial(0) == 1

def test_fatorial_de_um():
    assert fatorial(1) == 1

def test_fatorial_negativo():
    assert fatorial(-3) == "Erro: Fatorial de número negativo"