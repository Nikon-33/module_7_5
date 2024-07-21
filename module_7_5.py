import os
import time

# for dir in os.walk(r'C:\Обучение Python\UrbanAcademy\Обучение в Urban\7 Модуль'):
#     print(dir)

# for root, dirs, files  in os.walk(r'C:\Обучение Python\UrbanAcademy\Обучение в Urban\7 Модуль'):
#     print(f'Текущий каталог: {root}')
#     print(f'Подкаталоги: {dirs}')
#     print(f'Файлы: {files}')
#
# print(os.path.join('folder', 'subfolder', 'file.txt'))
#
#
# print('Время последнего изменения файла:', os.path.getmtime('products.txt'))
# print(os.path.dirname('/folder/subfolder/file.txt'))
# print('Размер файла в байтах: ', os.path.getsize('products.txt'))
# mod_time = os.path.getmtime('products.txt')
# print('Время последнего изменения файла: ', time.ctime(mod_time))

# после осмысления:
# не стал делать вывод в одну строку как показано в задании, потому что мне кажется так нагляднее и читабильнее
dir_path = r'C:\Обучение Python\UrbanAcademy\Обучение в Urban\7 Модуль'
for root, dirs, files in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        mod_time = os.path.getmtime(file_path)
        form_time = time.ctime(mod_time)
        size = os.path.getsize(file_path)

        print(f'Файл: {file_path}')
        print(f'Размер: {size} байт')
        print(f'Последнее изменение: {form_time}')
        print('-' * 40)
