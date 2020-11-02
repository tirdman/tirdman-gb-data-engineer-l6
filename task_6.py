"""
6. Создать НЕ! программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».

Проверить кодировку файла по умолчанию.

Принудительно!!!!! открыть файл в формате Unicode - encoding='utf-8'
и вывести его содержимое.

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но открыть нужно ИМЕННО в формате Unicode (utf-8)

например, with open('test_file.txt', encoding='utf-8') as t_f
невыполнение условия - минус балл
"""

from chardet import detect

# Определяем кодировку файла
with open('test_file.txt', 'rb') as t_f:
    content_byte = t_f.read()
    line_encode_detect = detect(content_byte)

print(f'Исходная кодировка файла: {line_encode_detect["encoding"]}')
print()

# При необходимости выполняем конвертацию
if line_encode_detect["encoding"] != 'utf-8':
    with open('test_file.txt', 'w', encoding='utf-8') as t_f:
        t_f.write(content_byte.decode(line_encode_detect["encoding"]))

# Главное условие задачи
with open('test_file.txt', encoding='utf-8') as t_f:
    content = t_f.read()
    print(content)
