def palindrome(word):
    word = word.lower()
    return word == word[::-1]

answer = input("Введите слово: ")
print(palindrome(answer))
