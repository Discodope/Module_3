def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower().upper() in i.lower().upper() or i.lower().upper() in root_word.lower().upper():
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Able', 'able', 'AbLe')
print(result2)