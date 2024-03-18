import pytest
from kalkulator_pytest import Kalkulator

@pytest.mark.parametrize("bilangan1, bilangan2, expected", [
    (5, 3, 8),
    (10, 5, 15),
    (-2, 4, 2),
])
def test_tambah(bilangan1, bilangan2, expected):
    # Arrange
    kalkulator = Kalkulator(bilangan1, bilangan2)

    # Act
    hasil = kalkulator.tambah()

    # Assert
    assert hasil == expected

@pytest.mark.parametrize("bilangan1, bilangan2, expected", [
    (5, 3, 2),
    (10, 5, 5),
    (-2, 4, -6),
])
def test_kurang(bilangan1, bilangan2, expected):
    # Arrange
    kalkulator = Kalkulator(bilangan1, bilangan2)

    # Act
    hasil = kalkulator.kurang()

    # Assert
    assert hasil == expected