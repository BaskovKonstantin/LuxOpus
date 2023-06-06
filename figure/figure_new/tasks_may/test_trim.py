def check_spelling(word):
    res = yaspeller.check(word, lang='ru').is_ok

    if not res.is_ok:
        return 1
    else:
        return 0


word = input("Введите слово: ")
result = check_spelling(word)
print(result)