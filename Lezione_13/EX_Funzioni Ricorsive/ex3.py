def recursiveFactorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursiveFactorial(n - 1)

print(recursiveFactorial(3))
print(recursiveFactorial(10))
print(recursiveFactorial(100))


