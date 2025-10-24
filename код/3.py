from re import *


text = input('Введите текст: ')

list_of_words = findall('[A-Za-zА-Яа-я]+', text)

words_and_nums = {}

for word in list_of_words:
    words_and_nums[word] = words_and_nums.get(word, 0) + 1

top5_words = []

for i in range(5):
    max_word = ''
    max_count = 0

    for word, current_count in words_and_nums.items():
        if current_count > max_count:
            max_word = word
            max_count = current_count
            
    top5_words.append((max_word, max_count))

    del words_and_nums[max_word]


print('5 самых частых слов: ')

for word, count_of_words in top5_words:
    print(f'{word}: {count_of_words}')   