import numpy as np

input = [[l for l in l.strip()] for l in open('./input').readlines()]

pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores2 = {'(': 1, '[': 2, '{': 3, '<': 4}
counter = 0
leaderboard = []

for row in input:
    toBeClosed = []
    for x in range(len(row)):
        if row[x] in scores2:
            toBeClosed.append(row[x])
        elif pairs[row[x]] == toBeClosed[-1]:  # If it matches the last one
            toBeClosed.pop()
        else:
            counter += scores[row[x]];
            break
        if x == len(row) - 1:  # If we got to the end w/o breaking:
            counter2 = 0
            toBeClosed.reverse()
            for item in toBeClosed:
                counter2 = counter2 * 5 + scores2[item]
            leaderboard.append(counter2)

print(counter, np.median(leaderboard))
