# 선택테스트 - 모음찾기

def find_vowel(character):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for char in character:
        if char in vowels:
            count += 1

    return count


character = "abracadabra"
print(find_vowel(character))

character2 = "aaaikoopelsuur"
print(find_vowel(character2))

