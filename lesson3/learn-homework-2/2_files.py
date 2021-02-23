"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

import textwrap

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print('Длина полученной на вход строки в символах:', len(content))
        print('В строку входит слов:', len(content.split()))
        content2 = content.replace('.', '!')
        with open('referat2.txt', 'w', encoding='utf-8') as output:
            output.write(content2)

if __name__ == "__main__":
    main()
