import importlib

module = importlib.import_module("36_most_frequent")

def test_most_frequent_standard():
    assert module.most_frequent([1, 3, 1, 3, 2, 1]) == 1

def test_most_frequent_empty():
    assert module.most_frequent([]) is None
