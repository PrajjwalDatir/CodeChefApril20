from sys import stdin


def isPrime(n):
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def strange_number():
    X, K = map(int, stdin.readline().split())
    total_di = 0
    if K == 1:
        if X > 1:
            print("1")
            return
        else:
            print("0")
            return
    if X == 1:
        if K == 0:
            print("1")
            return
        else:
            print("0")
            return
    else:
        i = 1
        while X != 1:
            i += 1
            if isPrime(i):
                while X % i == 0:
                    X = X // i
                    total_di += 1
                    if K <= total_di:
                        print("1")
                        return 0

        if K <= total_di:
            print("1")
            return
        else:
            print("0")
            return


T = int(stdin.readline())
for t in range(T):
    strange_number()

'''

'''
