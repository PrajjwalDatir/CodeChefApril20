from sys import stdin


def difSquare(n):
    return n % 4 != 2


def just_give_me_damn_output(seq, lengthhh):
    ans = 0
    # let's seq = [2,5,6]
    for i in range(lengthhh):  # for i to 0 to 3 means 0,1,2
        someNum = 1
        for j in range(i, lengthhh):  # j will be [0,1,2], [1, 2], [2]
            someNum *= abs(seq[j])
            # print(seq[k], end=" ")
            # print(someNum)
            if difSquare(someNum):
                ans += 1
    print(ans)


def square_sub():
    # count = 0  # to output the answer
    seq_size = int(stdin.readline())
    # pass all the combination of given sequence
    sequence = list(map(int, stdin.readline().split()))
    # need to find all combinations of the sequence
    # length = len(sequence)
    # myPowerSet(sequence, seq_size)
    just_give_me_damn_output(sequence, seq_size)


T = int(stdin.readline())
for t in range(T):
    square_sub()
