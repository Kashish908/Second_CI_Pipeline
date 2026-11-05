def is_pangram(s: str) -> bool:
    """Check if the given string is a pangram (contains all letters of the alphabet at least once)."""
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(s.lower()))
