# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os, time, shutil, re
global DEBUG
DEBUG = True


class FileTypeMove:
    def __init__(self, conditions, name, parent_directory, download_directory):
        self.conditions = conditions
        self.name = name
        self.files_list = []
        self.parent_directory = parent_directory
        self.download_directory = download_directory
        self.target_directory = self.parent_directory + 'downloaded_' + self.name

    def base_filter(self, file):
        for type in self.conditions:
            if type in file:
                return True
        return False

    def create_file_list(self, files):
        self.files_list = list(filter(self.base_filter, files))
        if DEBUG: print(self.name, self.files_list)

    def create_new_directory(self):
        if not os.path.isdir(self.target_directory + '/'):
            os.mkdir(self.target_directory)
            if DEBUG: print(self.name, "directory made")

    def move_files(self, files):
        self.create_file_list(files)
        self.create_new_directory()
        if self.files_list:
            for file in self.files_list:
                new_path = self.target_directory + '/' + file
                shutil.move(self.download_directory + '/' + file, new_path)
                if DEBUG: print(self.name, "moved", file, "from", self.download_directory, "to", new_path)

    def get_list(self):
        return self.files_list

    def rename(self):
        files = os.listdir(self.target_directory)
        self.create_file_list(files)
        if DEBUG: print("list files in", self.target_directory, self.files_list)
        for file in self.files_list:
            if DEBUG: print("rename", file[len(self.conditions[0])::])
            file_directory = self.target_directory + '/' + file
            new_name_file_directory = self.target_directory + '/' + file.replace(self.conditions[0], '')
            os.rename(file_directory, new_name_file_directory)




def moooove():
    if DEBUG: print(os.listdir())
    files = [file for file in os.listdir(downloadDirectory)]

    classwork = FileTypeMove(['__classwork__'], 'classwork', '', downloadDirectory)
    classwork.move_files(files)
    classwork.rename()

    images = FileTypeMove(['.png', '.jpg', 'jpeg', 'webp'], 'images', '', downloadDirectory)
    images.move_files(files)

    documents = FileTypeMove(['.docx', '.pdf', '.xls'], 'documents', '', downloadDirectory)
    documents.move_files(files)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #mac downloadDirectory = '/Users/vinhngo/Downloads'
    #windows downloadDirectory = 'C:/Users/vinh-school/Downloads'
    downloadDirectory = 'C:/Users/vinh-school/Downloads'
    moooove()

    """
    while(True):
        moooove()
        if DEBUG: print("mooove")
        time.sleep(5)
    """

# See PyCharm help at https://www.jetbrains.com/help/pycharm/