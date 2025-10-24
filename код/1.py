text = input('Введите текст: ')

list_of_words = []

word = ''

for i in text + ' ':
    if i != ' ':
        word += i
    else:
        list_of_words.append(word)
        word = ''

reversed_words = ''

for word in list_of_words:
    reversed_words = word + ' ' + reversed_words

reversed_text = ''

for i in text:
    reversed_text = i + reversed_text

print(f'{text} - {reversed_words}')
print(f'{text} - {reversed_text}')