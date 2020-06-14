import sys


def int1(x): return int(x) - 1
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def mi1(): return map(int1, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def lli(rows_number): return [li() for _ in range(rows_number)]


if __name__ == "__main__":