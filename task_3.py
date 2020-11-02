"""
3. Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- усложните задачу, "отловив" и обработав исключение
"""

words_list = ['attribute', 'класс', 'функция', 'type']

for next_word in words_list:
    try:
        next_word_byte = bytes(next_word, encoding="ascii")
        print(f'Слово "{next_word}" МОЖНО представить в байтовом формате')
    except UnicodeEncodeError as e:
        print(f'Слово "{next_word}" НЕЛЬЗЯ представить в байтовом формате')

