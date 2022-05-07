def solution(dirs):
    answer = 0
    path = []
    x = 0
    y = 0
    for i in dirs:
        if i == "U":
            if y < 5:
                if x + y < x + (y+1):
                    path.append(((x,y), (x,y+1)))
                else:
                    path.append(((x,y+1), (x,y)))
                y += 1
        elif i == "D":
            if y > -5:
                if x + y < x + (y-1):
                    path.append(((x,y), (x,y-1)))
                else:
                    path.append(((x,y-1), (x,y)))
                y -= 1
        elif i == "L":
            if x > -5:
                if x + y < (x-1) + y:
                    path.append(((x,y), (x-1,y)))
                else:
                    path.append(((x-1,y), (x,y)))
                x -= 1
        else:
            if x < 5:
                if x + y < (x+1) + y:
                    path.append(((x, y), (x+1,y)))
                else:
                    path.append(((x+1, y), (x,y)))
                x += 1
    sorted_path = sorted(path, key= lambda x: x[1], reverse=True)
    answer += len(set(path))
    return answer

dir = "ULURRDLLU"
dir2 = "LULLLLLLU"
dir3 = "UDU"
print(solution(dir))
print(solution(dir2))
print(solution(dir3))