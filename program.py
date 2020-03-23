import os


class FileOperations(object):
    def __init__(self):
        pass

    def get_available_num(self):
        list = os.listdir(os.getcwd())
        count = 0
        for x in list:
            if "test" in x:
                count += 1
        return count

    def is_file_available(self, name):
        files_list = os.listdir(os.getcwd())
        print(name)
        if name in files_list:
            return True
        return False

    def pick_the_file(self):
        print("Доступно", self.get_available_num(), " файлов")
        file = input("Введите номер файла, начиная с 0: ")
        if self.is_file_available("test" + file + ".txt"):
            return "test" + file + ".txt"
        print("Ошибка")
        return ""

