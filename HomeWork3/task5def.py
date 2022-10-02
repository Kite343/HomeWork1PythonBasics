def fibNegFib(n):
    fib = [0, 1]

    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])
    
    negFib = [-1 * fib[i] if i % 2 == 0 else fib[i] for i in range(1, n + 1)]

    return negFib[::-1] + fib

print(fibNegFib(8))