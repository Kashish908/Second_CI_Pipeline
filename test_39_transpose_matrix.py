import importlib

module = importlib.import_module("39_transpose_matrix")

def test_transpose_square():
    matrix = [[1, 2], [3, 4]]
    expected = [[1, 3], [2, 4]]
    assert module.transpose_matrix(matrix) == expected

def test_transpose_empty():
    assert module.transpose_matrix([]) == []
