def solution(w,h):
    answer = w * h
    lost_piece = 0

    if h > w:
        mok = h // 3
        nam = h % 3

        lost_piece = (mok * 4) + nam
    elif h < w:
        mok = w // 3
        nam = w % 3

        lost_piece = (mok * 4) + nam
    else:
        lost_piece = w

    return answer - lost_piece

w = 8
h = 12
print(solution(4, 3))
'''
실패!
'''
