def single_root_words(root_word,*other_words):
    same_words = []
    word = str(root_word).lower()
    other_words = list(map(str.lower , other_words))
    for i in range(len(other_words)):
        if word in other_words[i]:
            same_words.append(other_words[i])
            print(f'Слово {word} содержится в слове {other_words[i]}')
        if other_words[i] in word:
            same_words.append(other_words[i])
            print(f'Слово {other_words[i]} содержится в слове {word}')
    return same_words


result1 = single_root_words('word', 'swOrd', 'groups', 'root_word', 'tasks')
result2 = single_root_words('kit' , 'tools' , 'kitkat' , 'wood' , 'med_kit', 'kitchen')
result3 = single_root_words('Controls', 'trols' , 'ontr' , 'can' )
print('----------------------')
print(result1)
print(result2)
print(result3)


