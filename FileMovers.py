import os, shutil
from pathlib import Path
#import re

global DEBUG
DEBUG = True


class FileTypeMove:
    def __init__(self, folder_name, conditions, download_directory, target_directory):
        self.conditions = conditions
        self.folder_name = folder_name
        self.files_list = []
        self.download_directory = download_directory + '/'
        self.target_directory = target_directory + '/' + self.folder_name + '/'

    def type_filter(self, file):
        for file_type in self.conditions:
            if file_type in file:
                return True
        return False

    def create_file_list(self, files):
        self.files_list = list(filter(self.type_filter, files))
        if DEBUG: print(self.folder_name, "file list", self.files_list)

    def create_new_directory(self):
        if not os.path.isdir(self.target_directory):
            os.mkdir(self.target_directory)
            if DEBUG: print(self.folder_name, "directory made")

    def move_files(self, files):
        self.create_file_list(files)
        self.create_new_directory()
        if self.files_list:
            for file in self.files_list:
                new_path = self.target_directory + file
                shutil.move(self.download_directory + file, new_path)
                if DEBUG: print(self.folder_name, "moved", file, "from", self.download_directory, "to", new_path)

    def get_list(self):
        return self.files_list



class FileNameMove(FileTypeMove):
    def __init__(self, file_name, folder_name, conditions, download_directory, target_directory):
        super().__init__(folder_name, conditions, download_directory, target_directory)
        self.file_name = file_name
        self.rename_files = []


    def rename(self):
        if DEBUG: print("rename", self.folder_name)
        files = os.listdir(self.target_directory)
        self.create_file_list(files)
        if DEBUG: print("list files in", self.target_directory, self.files_list)
        for file in self.files_list:
            if DEBUG: print(self.folder_name, file[len(self.conditions[0])::])
            file_directory = self.target_directory + file
            new_name_file_directory = self.target_directory + file.replace(self.conditions[0], '')
            os.rename(file_directory, new_name_file_directory)



