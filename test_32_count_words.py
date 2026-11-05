def test_count_words_standard():
    # Dynamically reads and executes the program file to find the function
    namespace = {}
    with open("32_count_words.py", "r") as f:
        exec(f.read(), namespace)
    count_words = namespace["count_words"]
    
    assert count_words("The quick brown fox") == 4

def test_count_words_empty():
    namespace = {}
    with open("32_count_words.py", "r") as f:
        exec(f.read(), namespace)
    count_words = namespace["count_words"]
    
    assert count_words("") == 0