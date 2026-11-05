def most_frequent(arr):
    if not arr:
        return None
    # Use a dictionary to keep track of counts
    counts = {}
    for item in arr:
        counts[item] = counts.get(item, 0) + 1
    # Return the key with the maximum count value
    return max(counts, key=counts.get)
