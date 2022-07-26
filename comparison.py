from termcolor import cprint
import re

DATE_FORMAT = 'DD-MM-YYYY HH:MM:SS'

DATE_REGEX = r'(0[1-9]|1[0-9]|2[0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4}) ' \
             r'([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])'
PATH_REGEX = r'(?:[A-Z]:|\\|(?:\.{1,2}[\/\\]|\/)+)[\w+\\\(\)\/]+(?:\.\w+)*'


def compare_2_files(file_1, file_2):
    diff = []
    with open(file_1, mode='r', encoding='utf-8') as f1:
        f1_data = f1.readlines()
    with open(file_2, mode='r', encoding='utf-8') as f2:
        f2_data = f2.readlines()
    i = 0
    while i < len(f1_data) and i < len(f2_data):
        if f1_data[i] != f2_data[i]:
            print(f'{i}) {f1_data[i]}', end='')
            print(f'{i}) {f2_data[i]}')
            if is_path(f1_data[i], f2_data[i]):
                pass
            elif is_time(f1_data[i], f2_data[i]):
                pass
            else:
                diff.append(i)
        i += 1
    if diff:
        print('Найдены отличия в строках:')
        for dif in diff:
            print(f"- {dif}")
    else:
        print('Файлы отличаются только временем и местом сборки.')


def is_path(file_data_1, file_data_2):
    paths1 = re.findall(PATH_REGEX, file_data_1)
    paths2 = re.findall(PATH_REGEX, file_data_2)
    if paths1 != paths2:
        return True
    else:
        return False


def is_time(file_data_1, file_data_2):
    try:
        date1 = re.match(DATE_REGEX, file_data_1)
        date2 = re.match(DATE_REGEX, file_data_2)
        if date1 != date2:
            return True
        else:
            return False
    except AttributeError as exc:
        return False


if __name__ == '__main__':
    compare_2_files('zlib.1.2.11.log', 'zlib.1.2.12.log')
