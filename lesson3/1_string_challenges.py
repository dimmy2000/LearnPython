# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Последняя буква в слове {word} -', word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
counter = 0
for letter in word.lower():
    if letter == 'а':
        counter += 1
print(f'количество букв "а" в слове {word} -', counter)


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
counter = 0
for letter in word.lower():
    if letter in vowels:
        counter += 1
print(f'Количество гласных букв в слове {word} -', counter)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
word_count = sentence.split()
print(f'Количество слов в предложении "{sentence}" -', len(word_count))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for word in words:
    print(f'Первая буква {words.index(word)+1} слова предложения "{sentence}": {word[0]}')


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
some_words = sentence.split()
word_counter = 0
word_len_counter = 0
for word in some_words:
    word_counter += 1
    word_len_counter += len(word)
print(f'Средняя длина слова в предложении "{sentence}": ', int(word_len_counter/word_counter))
