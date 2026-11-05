def move_zeros(arr):
    # Filter out all non-zero elements
    non_zeros = [x for x in arr if x != 0]
    # Count how many zeros were present
    zero_count = len(arr) - len(non_zeros)
    # Combine non-zero elements with appended zeros
    return non_zeros + [0] * zero_count
