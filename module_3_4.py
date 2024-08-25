# Самостоятельная работа по уроку "Произвольное число параметров".


def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() in word.lower():
            same_words.append(word)
        if word.lower() in root_word.lower():
            same_words.append(word)
    return same_words


result = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)
