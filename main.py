from algorithm import NaiveStringInclude, StringBorder
from program import FileOperations


if __name__ == '__main__':
    answer = FileOperations.pick_the_file(FileOperations())
    if answer != "":
        """substring = input("Введите подстроку: ")
        naive = NaiveStringInclude(answer, substring)
        naive.check_text()"""

        naive = StringBorder(answer)
        naive.check_text()
