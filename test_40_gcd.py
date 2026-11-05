import importlib

module = importlib.import_module("40_gcd")

def test_gcd_standard():
    assert module.gcd(12, 18) == 6

def test_gcd_prime():
    assert module.gcd(7, 13) == 1
