import sys

def ii(): return int(sys.stdin.readline())
def li(): return list(map(int, sys.stdin.readline().split()))

if __name__ == "__main__":
    n = ii()
    a = li()
    a = sorted(a)
    a_max = a[-1]
    sive = [True] * (a_max + 1)

    def sived(x):
        for non_ans in range(x, a_max+1, x):
            sive[non_ans] = False
    ans = 0
    for i in range(len(a)-1):
        if sive[a[i]]:
            sived(a[i])
            if a[i] != a[i+1]:
                ans += 1
    if sive[a_max]:
        ans += 1
    print(ans)
