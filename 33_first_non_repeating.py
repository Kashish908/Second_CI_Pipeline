def first_non_repeating(string):
    # Count occurrences of each character
    counts = {}
    for char in string:
        counts[char] = counts.get(char, 0) + 1
        
    # Return the first character that appears exactly once
    for char in string:
        if counts[char] == 1:
            return char
            
    return None
