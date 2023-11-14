import os, shutil
from typing import List, Tuple
import logging
#import re

global DEBUG
DEBUG = True

IMAGES = ['.png', '.jpeg', '.jpg', '.webp', '.svg']
DOCUMENTS = ['.docx']
EXECS = ['.msi', '.exe', '.dmg']

class FileTypeMove: 
    def __init__(self, 
                 folder_name: str, 
                 source_dir: str,
                 target_dir: str,
                 file_types: List[List[str]],
                 file_name: str,
                 formatter: str,
                 sub_dir=[]
                 ):
        self.folder_name = folder_name
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.files_list = []
        self.file_types = type
        self.formatter = formatter
        self.sub_dir = sub_dir
        self.file_name = file_name

    def directory_to_list(self, dir: str) -> List[str]:
        return dir.split('/')[1::]
    
    def directory_to_string(self, dir: List[str]) -> str:
        result = ''
        for directory in dir:
            result += f"/{directory}"
        return result
    
    def create_new_directories(self, directory: List[str]) -> None:
        list_dir = self.directory_to_list(dir)
        if DEBUG: print(f"list of dir{directory}")
        for index, directory in enumerate(directory):
            dir = self.directory_to_string(directory[:index + 1])
            if DEBUG: print(f"dir = {dir}, index = {index}")
            if index > 0 and not os.path.isdir(dir):
                os.mkdir(dir)
                if DEBUG: print(f"created directory {dir}")

    def filter_by_name(self, files) -> List[str]:
        for file in files:
            file_name_list = file.split(self.formatter)
            if file_name_list[0].equals(self.file_name):
                return True
        return False
    
    def filter_by_type(self, files, file_type) -> List[str]:
        for file in files:
            file_name_list = file.split('.')
            if file_name_list[-1] in file_type:
                return True
        return False
    
    def filter_all(self, files) -> None:
        self.files_list = list(filter(self.filter_by_name, files))
        
    
    def dir_from_file(self, file) -> str:
        return file.split(self.formatter)[1:]
    
    def move_file(self, file):
        file_dir = self.dir_from_file(file)
        self.create_new_directory(file_dir)
        new_path = self.target_dir + file_dir
        shutil.move(self.source_dir + file, new_path)
        if DEBUG: print(f"{self.folder_name}: moved {file} from {self.source_dir} to {new_path}")