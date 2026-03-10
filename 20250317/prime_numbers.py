primes = []
for n in range(2, 101):
    is_prime = True
    for num in range(2, n):
        if n % num == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)

print("2에서 100사이의 소수들 : \n", primes)