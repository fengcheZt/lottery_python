import itertools
# print(list(itertools.combinations([1,2,3,4],3)))

values = []
redBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31, 32, 33]
blueBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
redList = list(itertools.combinations(redBall, 6))
for i in redList:
    for j in blueBall:
        ij = i + (j,)
        values.append(ij)
print(len(values))