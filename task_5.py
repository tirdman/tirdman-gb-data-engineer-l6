"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet!!!
"""

import subprocess
from chardet import detect

url_ping_list = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for next_ping in url_ping_list:
    ping = subprocess.Popen(next_ping, stdout=subprocess.PIPE)
    for line_byte in ping.stdout:
        line_encode_detect = detect(line_byte)
        line_str = line_byte.decode(line_encode_detect['encoding'])
        print(line_str, end='')
