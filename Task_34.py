# Ритм есть, если число слогов (гласных букв) в каждой фразе стихотворения одинаковое.
# Фразы отделяются друг от друга пробелами.
# Если во фразе несколько слов, то они разделяются дефисами.
# “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

poem = input('Ввод стихотворения: ')

vowels = 'АЕЁИОУЫЭЮЯаеёиоуыэюя'
num_vowels = []
for phrase in poem.split():
    count = 0
    for letter in phrase:
        if letter in vowels:
            count += 1
    num_vowels.append(count)

if all(elem == num_vowels[0] for elem in num_vowels):
    print('Парам пам-пам')
else:
    print('Пам парам')
