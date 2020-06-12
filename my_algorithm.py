from typing import List


def prime_factorize(n: int) -> List[int]:
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def prime_number_enumerate(n: int) -> List[int]:
    prime_list = []
    search_list = list(range(2, n+1))
    head = 2
    while head * head <= n:
        head = search_list[0]
        prime_list.append(head)
        search_list = [num for num in search_list if num % head != 0]
    prime_list.extend(search_list)
    return prime_list


if __name__ == "__main__":
    print(prime_number_enumerate(1))
