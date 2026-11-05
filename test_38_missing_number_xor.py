import importlib

module = importlib.import_module("38_missing_number_xor")

def test_missing_number_standard():
    # n = 5, numbers should be 1 to 5. Missing 3.
    assert module.find_missing_number([1, 2, 4, 5], 5) == 3

def test_missing_number_first():
    # n = 3, numbers should be 1 to 3. Missing 1.
    assert module.find_missing_number([2, 3], 3) == 1
