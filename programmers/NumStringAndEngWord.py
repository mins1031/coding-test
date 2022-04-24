def solution(s):
    word = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    num = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
           '8': '8', '9': '9'}
    temp = []
    dumy_str = ""
    for i in range(len(s)):
        if s[i] in num:
            temp.append(num[s[i]])
        else:
            dumy_str += s[i]

        if dumy_str in word:
            temp.append(word[dumy_str])
            dumy_str = ""

    answer = ''.join(temp)
    return int(answer)