import pytest
from calcular_pontos import calcular_pontos

def test_compras_na_rede_x_com_cartao_x():
    assert calcular_pontos(150.75, True, True) == 450  # 150 * 3 = 450
    assert calcular_pontos(200.99, True, True) == 600  # 200 * 3 = 600
    assert calcular_pontos(0.99, True, True) == 0       # 0 * 3 = 0

def test_compras_na_rede_x_sem_cartao_x():
    assert calcular_pontos(150.75, True, False) == 225  # 150 * 1.5 = 225
    assert calcular_pontos(200.99, True, False) == 300  # 200 * 1.5 = 300
    assert calcular_pontos(0.99, True, False) == 0       # 0 * 1.5 = 0

def test_compras_fora_da_rede_x_com_cartao_x():
    assert calcular_pontos(150.75, False, True) == 150  # 150 * 1 = 150
    assert calcular_pontos(200.99, False, True) == 200  # 200 * 1 = 200
    assert calcular_pontos(0.99, False, True) == 0       # 0 * 1 = 0

def test_compras_fora_da_rede_x_sem_cartao_x():
    assert calcular_pontos(150.75, False, False) == 0  # Sem pontos
    assert calcular_pontos(200.99, False, False) == 0  # Sem pontos
    assert calcular_pontos(0.99, False, False) == 0     # Sem pontos

# Executar os testes
if __name__ == "__main__":
    pytest.main()
