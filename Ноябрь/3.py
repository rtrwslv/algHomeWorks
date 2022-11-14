def findWay(path):
    result = 0
    flag = False
    if path[0][0] == 1:
        return 0
    for i in range(1, len(path)):
        if path[i][0] == 1:
            flag = True
    if not flag:
        if 1 not in path[-1]:
            result += 1
    flag = False
    if 1 not in path[0] and 1:
        for i in range(len(path)):
            if path[i][-1] == 1:
                flag = True
        if not flag:
            result += 1
    print(result)
findWay([[0,1],[0,0]])