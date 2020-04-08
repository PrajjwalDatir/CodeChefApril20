'''
T denoting the number of test cases
N , M , K where #N is total questions #M is the total options to each question #K is the number of sets
C11 C12   #for K=2 N=4 M=2
C21 C22
C31 C32
C41 C42
'''

import random
import sys


def reset_ppo(le):
    something = []
    for j_iter in range(le):
        something.append(0)
    return something


def leaked_answers(N, M, K):
    # output = []
    # full_score = []
    # current_min = 0
    marks_per_set_col = reset_ppo(K)
    for j_iter in range(N):
        point_per_option_row = reset_ppo(M)
        answers = list(sys.stdin.readline().split())
        for k_iter in range(K):
            # print(k_iter)
            point_per_option_row[int(answers[k_iter]) - 1] += 1
        # best_option = point_per_option_row.index(max(point_per_option_row))
        best_option = [i for i, x in enumerate(point_per_option_row) if x == max(point_per_option_row)]
        best_option = list(map(lambda x: x + 1, best_option))
        # full_score = list(map(lambda x: x + best_option, full_score))
        # print(best_option, end="hello is it working??\n")
        # for other_iter in range(len(best_option)):
            # for some_iter in range(K):
                # if int(answers[some_iter]) == best_option[other_iter]:
                    # marks_per_set_col[some_iter] += 1
                    # print(f"222here answer set is : {answers}")
                    # current_min = min(marks_per_set_col)
                # print(output, end=":output")
            # print(marks_per_set_col, end=":000marks_per_set\n")
        # for new_iter in best_option:
        print(best_option[random.randint(0, len(best_option) - 1)], end=" ")
        # output.append(best_option[other_iter])
    # print(output, end="this is output\n")


test_cases = int(sys.stdin.readline())
for i_iter in range(test_cases):
    sec_line = list(sys.stdin.readline().split())
    NN = int(sec_line[0])
    MM = int(sec_line[1])
    KK = int(sec_line[2])
    leaked_answers(NN, MM, KK)
