def is_sorted(arr):
    # An empty array or array with one element is always sorted
    if len(arr) <= 1:
        return True

    # Check if every element is less than or equal to the next one
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True
