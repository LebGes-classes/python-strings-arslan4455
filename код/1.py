text = input('Введите текст: ')

list_of_words = []

word = ''

for sym in text + ' ':
    if sym == ' ':
        list_of_words.append(word)
        word = ''
    else:
        word += sym

reversed_words = ''

for word in list_of_words:
    reversed_words = word + ' ' + reversed_words

reversed_text = ''

for i in text:
    reversed_text = i + reversed_text

print(f'{text} - {reversed_words}')
print(f'{text} - {reversed_text}')