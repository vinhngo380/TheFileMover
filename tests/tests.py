import logging
import unittest
from FileMover.FileMoversV2 import FileTypeMove, IMAGES

class TestFileTypeMove(unittest.TestCase):
    def test_directory_to_list(self):
        test = FileTypeMove('test_folder', '', '', IMAGES)
        list = test.directory_to_list('/Users/Documents/Test 1/Test2')
        self.assertEqual(list, ['Users', 'Documents', 'Test 1', 'Test2'])

    def test_directory_to_string(self):
        test = FileTypeMove('test_folder', '', '', IMAGES)
        string = test.directory_to_string(['Users', 'Documents', 'Test 1', 'Test2'])
        self.assertEqual(string, '/Users/Documents/Test 1/Test2')




if __name__ == '__main__':
    unittest.main(verbosity=2)
