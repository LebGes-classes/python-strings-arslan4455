from re import *


text = input('Введите текст: ')

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

text = text[0:-1] + ' '

list_of_words = []

word = ''

for sym in text:
    if sym == ' ':
        list_of_words.append(word)
        
        word = ''
    else:
        word += sym
    
k = 0

for word in list_of_words:
    if len(word) >= k:
        k = len(word)

new_text = ''

for i in text:
    if i in lower:
        new_sym = lower[(lower.index(i) + k) % 26]

        new_text += new_sym
    elif i in upper:
        new_sym = upper[(upper.index(i) + k) % 26]

        new_text += new_sym
    else:
        new_text += i
    
print(f'Шифр: {new_text}')
print(f'k = {k}')
    