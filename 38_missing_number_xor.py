def find_missing_number(arr, n):
    # XOR all numbers from 1 to n
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i

    # XOR all numbers present in the array
    xor_arr = 0
    for num in arr:
        xor_arr ^= num

    # The missing number is the XOR of both results
    return xor_all ^ xor_arr
