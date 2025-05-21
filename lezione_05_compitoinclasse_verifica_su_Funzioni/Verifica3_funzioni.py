def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 2
        if n > 1:
            factors.append(n)
        return factors
print(prime_factors(4))
print(prime_factors(76))