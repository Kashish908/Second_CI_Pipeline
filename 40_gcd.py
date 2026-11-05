def gcd(a, b):
    # Euclidean algorithm to find the greatest common divisor
    while b:
        a, b = b, a % b
    return a
