def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        tmp = [0 for _ in range(len(skill))]
        for j in range(len(skill)):
            if skill[j] in i:
                idx = i.index(skill[j]) + 1
                tmp[j] = idx
        for i in range(1, len(tmp)):
            if tmp[i] == 0:
                continue
            if tmp[i] < tmp[i-1] or (tmp[i] != 0 and tmp[i-1] == 0):
                break
        else:
            answer += 1

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA", "CXF", "ASF", "CEFD"]
print(solution(skill, skill_trees))