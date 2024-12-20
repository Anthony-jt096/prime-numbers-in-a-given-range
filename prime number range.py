def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    prime_list = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list


start = 1
end = 100


primes = find_primes_in_range(start, end)


print(f"Prime numbers between {start} and {end}:")
print(primes)




          




          