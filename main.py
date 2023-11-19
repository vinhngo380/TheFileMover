
import time, os
from FileMover.FileMovers import FileMover as FileMover, IMAGES
from pathlib import Path, PurePath

DOWNLOAD_DIRECTORY = str(Path.home() / "Downloads") #C:\Users\user_name\Downlaods
DOCUMENTS_DIRECTORY = str(Path.home() / "Documents") #C:\Users\user_name\Documents

global DEBUG
DEBUG = True

if __name__ == '__main__':
    test_path = PurePath('/Users/Vinh/Documents/Test 1/Test2/He He He Ha/')

    test = FileMover('test_folder', PurePath(DOWNLOAD_DIRECTORY), test_path, [IMAGES], ['tester'])
    print(test.target_directory, type(test.target_directory))
    test.create_new_directories(test.target_directory)
    test.move_files()

