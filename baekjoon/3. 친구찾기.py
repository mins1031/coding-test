def find_friend(names):
    result = []
    for i in names:
        if len(i) == 4:
            result.append(i)

    return result


names = ["Ryan", "Kieran", "Mark", "Sam", "Peter", "Rosa"]
print(find_friend(names))
