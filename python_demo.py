def is_prime(n):
    i = 2
    while i <= n:
        if n % i == 0:
            if i != n:
                return False
            
        i += 1

    return True

print(is_prime(8))