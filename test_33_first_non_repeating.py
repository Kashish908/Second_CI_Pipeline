import importlib

# Standard Python import hook for filenames starting with numbers
module = importlib.import_module("33_first_non_repeating")

def test_found():
    # 'w' is the first non-repeating character in 'swiss'
    assert module.first_non_repeating("swiss") == "w"

def test_not_found():
    # All characters repeat in 'aabbcc'
    assert module.first_non_repeating("aabbcc") is None
