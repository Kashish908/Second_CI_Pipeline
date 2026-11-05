import importlib

module = importlib.import_module("34_check_sorted")

def test_sorted_true():
    assert module.is_sorted([1, 2, 3, 4, 5]) is True

def test_sorted_false():
    assert module.is_sorted([1, 3, 2, 4, 5]) is False
