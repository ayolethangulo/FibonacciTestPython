import pytest

def test_primera_posicion():
    assert sumar_posicion(1)==0

def test_segunda_posicion():
    assert sumar_posicion(2)==1

def test_validar_mayor_cero():
    assert sumar_posicion(-5)==-1

def sumar_posicion(posicion):
    if posicion == 1:
        return 0
    elif posicion == 2:
        return 1
