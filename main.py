
import os
from time import time
from FileMover.FileMovers import FileMover as FileMover, IMAGES, DOCUMENTS, EXECS
from pathlib import Path, PurePath

DOWNLOAD_DIRECTORY = str(Path.home() / "Downloads") #C:\Users\user_name\Downlaods
DOCUMENTS_DIRECTORY = str(Path.home() / "Documents") #C:\Users\user_name\Documents

global DEBUG
DEBUG = True

if __name__ == '__main__':
    test_path = PurePath('/Users/Vinh/Documents/Test 1/Test2/He He He Ha/')
    testing_path = Path(PurePath(os.path.join(DOCUMENTS_DIRECTORY, 'Test 1/Test2/He He He Ha/')))
    testing_path.mkdir(parents=True, exist_ok=True)
    print("walk completed")
    print(f"images, execs, and documents {[IMAGES, EXECS, DOCUMENTS]}")
    test = FileMover('test_folder', PurePath(DOWNLOAD_DIRECTORY), test_path, [IMAGES, DOCUMENTS, EXECS], ['tester'])
    # print(f"create_regex_name: {test.create_file_regex()}")
    start = time()
    hi = test.filter_test2()
    end = time()
    time_filter_test2 = end - start
    print(f'filter_test2: {time_filter_test2}')

    start = time()
    files = os.listdir(DOWNLOAD_DIRECTORY)
    test.filter_all(files)
    end = time()
    time_filter_all = end - start
    print(f'filter_all: {time_filter_all}')

    print(f'ratio of test2/all: {time_filter_test2/time_filter_all}')
