# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time
from FileMovers import *

global DEBUG
DEBUG = True


def mooove(dled_files):
    compeng270.move_files(dled_files)
    compeng270.rename()

    math220.move_files(dled_files)
    math220.rename()

    physics212.move_files(dled_files)
    physics212.rename()

    classwork.move_files(dled_files)
    classwork.rename()

    images.move_files(dled_files)
    documents.move_files(dled_files)

    execs.move_files(dled_files)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    taken from https://stackoverflow.com/questions/35851281/python-finding-the-users-downloads-folder
    not the best solution --> it will not work for people who do not use english and move their downloads folder around, but its not really a big concern unless i let other people use this
    """
    dl_dir = str(Path.home() / "Downloads")

    sdocs_target_dir = str(Path.home() / "Documents") + '/Schoolwork/Semester 3'

    if DEBUG: print(os.listdir())
    files = [file for file in os.listdir(dl_dir)]

    classwork = FileNameMove('__classwork__', 'classwork', ['__classwork__'], dl_dir, '')
    images = FileTypeMove('images', ['.png', '.jpg', 'jpeg', 'webp'], dl_dir, '')
    documents = FileTypeMove('documents', ['.docx', '.pdf', '.xls'], dl_dir, '')
    execs = FileTypeMove('execs', ['.exe', '.app', '.msi'], dl_dir, dl_dir)

    compeng270 = FileNameMove('_ce270_', 'Comp Eng 270', ['_ce270_'], dl_dir, sdocs_target_dir)
    physics212 = FileNameMove('_p212_', 'Physics 212', ['_p212_'], dl_dir, sdocs_target_dir)
    math220 = FileNameMove('_m220_', 'Math 220', ['_m220_'], dl_dir,
                           sdocs_target_dir)

    mooove(files)

    """
    while(True):
        mooove()
        if DEBUG: print("mooove")
        time.sleep(60)
    """

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
