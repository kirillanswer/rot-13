"""
Шахов Кирилл ИВТ 2 курс
Задание реализовать шифр Цезаря (rot 13) со считыванием из файла и записи в новый результата
"""

def rot13(a):
    def transform(pyf):
        index = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.find(pyf)
        if index != -1:
            return 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'[index]
        else:
            return pyf

    return "".join(map(transform, a))

my_file = open("some.txt", "r")
my_string = my_file.read()
my_file.close()

my_file1 = open("some1.txt", "a+")
a = (rot13(my_string))
my_file1.write(a)
my_file1.write("\n")
my_file1.close()
