import logging
import unittest
from FileMover.FileMoversV2 import FileTypeMove, IMAGES

class TestFileTypeMove(unittest.TestCase):
    def test_directory_to_list(self):
        test = FileTypeMove('test_folder', '', '', [IMAGES], 'tester')
        list = test.directory_to_list('/Users/Documents/Test 1/Test2')
        self.assertEqual(list, ['Users', 'Documents', 'Test 1', 'Test2'])

    def test_directory_to_string(self):
        test = FileTypeMove('test_folder', '', '', [IMAGES], 'tester')
        string = test.directory_to_string(['Users', 'Documents', 'Test 1', 'Test2'])
        self.assertEqual(string, '/Users/Documents/Test 1/Test2')

    def test_filter_by_name(self):
        file_test = ['test.png', 'oof.pdf', 'tester.ty.jpg', 'tester_hello.png', 'tester_e.docx', 'tester_tsdf.pdf']
        test = FileTypeMove('test_folder', '', '', [IMAGES], 'tester')
        result = list(filter(test.filter_by_name, file_test))
        self.assertEqual(result, ['tester_hello.png', 'tester_e.docx', 'tester_tsdf.pdf'])

    def test_filter_by_type(self):
        file_test = ['test.png', 'oof.pdf', 'tester.ty.jpg', 'tester_hello.png', 'tester_e.docx', 'tester_tsdf.pdf']
        test = FileTypeMove('test_folder', '', '', [IMAGES], 'tester')
        result = list(filter(test.filter_by_type, file_test))
        self.assertEqual(result, ['test.png', 'tester.py.jpg', 'tester_hello.png'])




if __name__ == '__main__':
    unittest.main(verbosity=2)
