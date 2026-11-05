import importlib

module = importlib.import_module("37_rotate_string")

def test_rotate_standard():
    assert module.rotate_string("hello", 2) == "lohel"

def test_rotate_zero():
    assert module.rotate_string("abc", 0) == "abc"
