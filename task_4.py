"""
4. Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words_list = ['разработка', 'администрирование', 'protocol', 'standard']

for next_word in words_list:
    next_word_to_byte = next_word.encode(encoding='utf-8')
    print(f"Слово '{next_word}' в байты: {next_word_to_byte}")

    next_word_from_byte = next_word_to_byte.decode(encoding='utf-8')
    print(f"Из байтов: '{next_word_from_byte}'")

    print()
