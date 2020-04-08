testCases = int(input())
totalPeople = []
Queue = []

for i in range(testCases):
    Legal = 6
    temp = int(input())
    totalPeople = (input().split())
    result = "YES"

    for j in totalPeople:
        #print(totalPeople[i])
        #print(i)
        j = int(j)
        if j == 1 and Legal >= 6:
            Legal = 1
            continue
        elif j == 1 and Legal < 6:
            result = "NO"
            break
        elif j == 0:
            Legal = Legal + 1
            continue
    if result == "NO":
        print(result)
    else:
        print(result)