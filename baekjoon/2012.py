student_count = int(input())
scores = list()
for i in range(student_count):
    scores.append(int(input()))

scores.sort()

discontent = 0
for i in range(1, student_count+1):
    discontent += abs(i - scores[i-1])

print(discontent)