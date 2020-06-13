from typing import List


def prime_factorize(n: int) -> List[int]:
    factor_list = []
    while n % 2 == 0:
        factor_list.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            factor_list.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        factor_list.append(n)
    return factor_list


def prime_number_enumerate(maximum):
    sieve = [True] * (maximum + 1)

    def sieved(prime):
        for not_prime in range(prime + prime, maximum + 1, prime):
            sieve[not_prime] = False

    sieve[0] = sieve[1] = False
    sieved(2)
    for x in range(3, int(maximum ** 0.5) + 1, 2):
        if sieve[x]:
            sieved(x)
    return [prime for prime, is_prime in enumerate(sieve) if is_prime]


if __name__ == "__main__":
    print(prime_factorize(1296))
