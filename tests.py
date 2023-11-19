import logging
import unittest, os
from FileMover.FileMoversV2 import FileMover, IMAGES
from pathlib import Path

DOWNLOAD_DIRECTORY = str(Path.home() / "Downloads")
DOCUMENTS_DIRECTORY = str(Path.home() / "Documents")

class TestFileMover(unittest.TestCase):
    def test_directory_to_list(self):
        test = FileMover('test_folder', '', '', [IMAGES], ['tester'])

        test_string = '/Users/Documents/Test 1/Test2'
        list = test.directory_to_list(test_string)
        print(os.path.split(test_string))
        self.assertEqual(list, ['Users', 'Documents', 'Test 1', 'Test2'])

        list = test.directory_to_list('')
        self.assertEqual(list, [])
        
        test_string = f"{DOCUMENTS_DIRECTORY}/Test 1/Test2/pew_pew"
        list = test.directory_to_list(test_string)
        norm_path_string = os.path.normpath(test_string)
        print(DOWNLOAD_DIRECTORY, list, norm_path_string)
        print(test.directory_to_list(norm_path_string))
        print(os.path.splitdrive(norm_path_string))

    def test_directory_to_string(self):
        test = FileMover('test_folder', '', '', [IMAGES], ['tester'])
        
        string = test.directory_to_string(['Users', 'Documents', 'Test 1', 'Test2'])
        self.assertEqual(string, '/Users/Documents/Test 1/Test2')

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




if __name__ == '__main__':
    unittest.main(verbosity=2)
