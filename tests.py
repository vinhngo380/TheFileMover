import logging
import unittest, os
from FileMover.FileMovers import FileMover, IMAGES
from pathlib import Path, PurePath

DOWNLOAD_DIRECTORY = str(Path.home() / "Downloads") #C:\Users\user_name\Downlaods
DOCUMENTS_DIRECTORY = str(Path.home() / "Documents") #C:\Users\user_name\Documents

class TestFileMover(unittest.TestCase):
    def test_directory_to_list(self):
        
        test = FileMover('test_folder', '', '', [IMAGES], ['tester'])

        test_string = '/Users/Documents/Test 1/Test2'
        list = test.string_to_tuple(test_string)
        print(os.path.split(test_string))
        self.assertEqual(list, ('Users', 'Documents', 'Test 1', 'Test2'))

        list = test.string_to_tuple('')
        self.assertEqual(list, ())

        test_string = f"{DOCUMENTS_DIRECTORY}/Test 1/Test2"
        list = test.string_to_tuple(test_string)
        self.assertEqual(list, ('Users', os.getlogin(), 'Documents', 'Test 1', 'Test2')) #Windows

    def test_directory_to_string(self):
        test = FileMover('test_folder', '', '', [IMAGES], ['tester'])
        
        test_string = test.tuple_to_string(('Users', 'Documents', 'Test 1', 'Test2'))
        self.assertEqual(test_string, 'Users\\Documents\\Test 1\\Test2')

    def test_filter_by_name(self):
        test = FileMover('test_folder', '', '', [IMAGES], ['tester'])

        file_test = ['test.png', 'oof.pdf', 'tester.ty.jpg', 'tester_hello.png', 'tester_e.docx', 'tester_tsdf.pdf']
        result = test.filter_by_name(file_test)
        self.assertEqual(result, ['tester_hello.png', 'tester_e.docx', 'tester_tsdf.pdf'])

        file_test = []
        result = test.filter_by_name(file_test)
        self.assertEqual(result, [])

    def test_filter_by_type(self):
        test = FileMover('test_folder', '', '', [IMAGES], ['tester'])

        file_test = ['test.png', 'oof.pdf', 'tester.ty.jpg', 'tester_hello.png', 'tester_e.docx', 'tester_tsdf.pdf']
        result = test.filter_by_type(file_test)
        self.assertEqual(result, ['test.png', 'tester.ty.jpg', 'tester_hello.png'])

        test = FileMover('test_folder', '', '', [], ['tester'])
        file_test = ['test.png', 'oof.pdf', 'tester.ty.jpg', 'tester_hello.png', 'tester_e.docx', 'tester_tsdf.pdf']
        result = test.filter_by_type(file_test)
        self.assertEqual(result, [])

    def test_filter_all(self):
        test = FileMover('test_folder', '', '', [IMAGES], ['tester'])

        file_test = ['test.png', 'oof.pdf', 'tester.ty.jpg', 'tester_hello.png', 'tester_e.docx', 'tester_tsdf.pdf']
        result = test.filter_by_type(file_test)
        self.assertEqual(result, ['test.png', 'tester.ty.jpg', 'tester_hello.png'])

        test = FileMover('test_folder', '', '', [], ['tester'])
        result = test.filter_by_type(file_test)
        self.assertEqual(result, [])

    def test_printing_lol(self):
        # test = FileMover('test_folder', '', '', [IMAGES], ['tester'])
        # test_string = f"{DOCUMENTS_DIRECTORY}/Test 1/Test2/pew_pew"
        # list = test.directory_to_list(test_string)
        # norm_path_string = os.path.normpath(test_string)

        # print(DOWNLOAD_DIRECTORY, list, norm_path_string)
        # print(test.directory_to_list(norm_path_string))
        # print(os.path.splitdrive(norm_path_string))
        # print(os.path.join(DOCUMENTS_DIRECTORY, '/Test 1/Test2/pew_pew'))
        # print(os.getlogin())
        # print(os.path.join(*['Users', os.getlogin(), 'Documents', 'Test 1', 'Test2']))
        # print(*['test1', 'test2', 'test3'])
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
