import os, shutil
from typing import List


global DEBUG
DEBUG = False

IMAGES = ['png', 'jpeg', 'jpg', 'webp', 'svg']
DOCUMENTS = ['docx']
EXECS = ['msi', 'exe', 'dmg']

class FileMover:
    #'.' is not a valid format as of right now because of filter_by_type
    def __init__(self, 
                 folder_name: str, 
                 source_directory: str,
                 target_directory: str,
                 file_types: List[List[str]],
                 valid_file_name: List[str],
                 formatter ='_', 
                 sub_dir=[]
                 ):
        self.folder_name = folder_name
        self.source_directory = source_directory
        self.target_directory = target_directory
        self.files_list = []
        self.file_types = file_types
        self.formatter = formatter
        self.sub_dir = sub_dir
        self.valid_file_name = valid_file_name

    def directory_to_list(self, dir: str) -> List[str]:
        return dir.split('/')[1::]
    
    def directory_to_string(self, dir: List[str]) -> str:
        result = ''
        for directory in dir:
            result += f"/{directory}"
        return result
    
    def create_new_directories(self, directory: str) -> None:
        list_dir = self.directory_to_list(directory)
        if DEBUG: print(f"list of dir{list_dir}")
        for index, directory in enumerate(directory):
            dir = self.directory_to_string(directory[:index + 1])
            if DEBUG: print(f"dir = {dir}, index = {index}")
            if index > 0 and not os.path.isdir(dir):
                os.mkdir(dir)
                if DEBUG: print(f"created directory {dir}")

    def filter_by_name(self, files: List[str]) -> List[str]:
        files_filtered = []
        for file in files:
            file_name_list = file.split(self.formatter)[0]
            if DEBUG: print(f"file = {file_name_list} file_name = {self.valid_file_name}")
            if file_name_list in self.valid_file_name:
                files_filtered.append(file)
        return files_filtered
    
    def filter_by_type(self, files: List[str]) -> List[str]:
        flattened_valid_file_types = [] 
        for sub_valid_type in self.file_types:
            for valid_file_type in sub_valid_type:
                flattened_valid_file_types.append(valid_file_type)

        files_filtered = []
        for file in files:
            file_type = file.split('.')[-1]
            if DEBUG: print(f"file_type = {file_type} valid_file_types = {flattened_valid_file_types}")
            if file_type in flattened_valid_file_types:
                files_filtered.append(file)
        return files_filtered
    
    def filter_all(self, files) -> None:
        temp = self.filter_by_name(files)
        self.files_list = self.filter_by_type(temp)

    def dir_from_file(self, file: str) -> str:
        return file.split(self.formatter)[1:]
    
    def move_file(self, file: str) -> None:
        file_dir = self.dir_from_file(file)
        self.create_new_directories(file_dir)
        new_path = self.target_directory + file_dir
        shutil.move(self.source_directory + file, new_path)
        if DEBUG: print(f"{self.folder_name}: moved {file} from {self.source_directory} to {new_path}")

    def add_file_types(self, new_file_types: List[str]) -> None:
        # if not isinstance(new_file_types, List):
        #     pass
        self.file_types.append(new_file_types)

    def add_valid_name(self, new_file_names: List[str]) -> None:
        self.valid_file_name.append(new_file_names)