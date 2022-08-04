def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)


answer1 = input("Введите первое слово: ")
answer2 = input("Введите второе слово: ")
print(anagram(answer1, answer2))
