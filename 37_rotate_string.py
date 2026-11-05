def rotate_string(s, k):
    if not s:
        return s
    # Ensure k is within bounds of string length
    k = k % len(s)
    # Rotate the string to the right by k positions
    return s[-k:] + s[:-k]
