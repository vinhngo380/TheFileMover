import os, shutil
from typing import List, Tuple
from pathlib import PurePath


global DEBUG
DEBUG = True

IMAGES = ['png', 'jpeg', 'jpg', 'webp', 'svg']
DOCUMENTS = ['docx']
EXECS = ['msi', 'exe', 'dmg']

class FileMover:
    #'.' is not a valid format as of right now because of filter_by_type
    def __init__(self, 
                 folder_name: str, 
                 source_directory: PurePath,
                 target_directory: PurePath,
                 file_types: List[List[str]],
                 valid_file_name: List[str],
                 formatter ='_', 
                 sub_dir=[]
                 ):
        self.folder_name = folder_name
        self.source_directory = source_directory
        self.target_directory = PurePath(os.path.normpath(os.path.join(target_directory, folder_name)))
        self.files_list = []
        self.file_types = self.add_file_types(file_types)
        self.formatter = formatter
        self.sub_dir = sub_dir
        self.valid_file_names = self.add_file_types(valid_file_name)

    def string_to_tuple(self, dir: str) -> Tuple[str]:
        if DEBUG: print(f"directory_to_list: {os.path.normpath(dir)}")
        path_object_dir = PurePath(os.path.normpath(dir))
        return path_object_dir.parts[1::]
    
    def tuple_to_string(self, dir: Tuple[str]) -> str:
        path_object_dir = os.path.normpath(os.path.join(*dir))
        return path_object_dir
    
    def create_new_directories(self, directory: PurePath) -> None:
        print(f"create_new_directories: {directory}")
        path_list = directory.parents
        for i in range(len(path_list) - 2, -1, -1): #make this more dynamic
            current_path = PurePath(path_list[i])
            print(str(current_path))
            if not os.path.isdir(current_path):
                os.mkdir(current_path)
        if not os.path.isdir(directory):
            os.mkdir(directory)

    def filter_by_name(self, files: List[str]) -> List[str]:
        files_filtered = []
        for file in files:
            file_name_list = file.split(self.formatter)[0]
            if DEBUG: print(f"file = {file_name_list} file_name = {self.valid_file_names}")
            if file_name_list in self.valid_file_names:
                files_filtered.append(file)
        return files_filtered
    
    def filter_by_type(self, files: List[str]) -> List[str]:
        files_filtered = []
        for file in files:
            file_type = file.split('.')[-1].lower()
            if DEBUG: print(f"file = {file} file_type = {file_type} file_type type = {type(file_type)} conditional: {file_type in flattened_valid_file_types}")
            if file_type in self.file_types:
                files_filtered.append(file)
        return files_filtered
    
    def filter_all(self, files) -> None:
        temp = self.filter_by_name(files)
        if DEBUG: print(f"filter_all: filtered by name = {temp}")
        self.files_list = self.filter_by_type(temp)

    def dir_from_file(self, file: str) -> str:
        return file.split(self.formatter)[1::-2]
    
    def move_file(self, file: str) -> None:
        file_dir = ''
        # file_dir = self.dir_from_file(file)
        # self.create_new_directories(file_dir)
        new_path = os.path.join(self.target_directory, file)
        print(f"move_file: source_dir = {self.source_directory} type = {type(self.source_directory)}", *self.source_directory.parts)
        file_path = PurePath(os.path.normpath(os.path.join(*self.source_directory.parts, file)))
        if DEBUG: print(f"move_file: folder_name = {self.folder_name} file = {file} paths = {file_path} to {new_path}")
        shutil.move(file_path, new_path)
        if DEBUG: print(f"{self.folder_name}: moved {file} from {file_path} to {new_path}")

    def move_files(self) -> None:
        file_list = os.listdir(self.source_directory)
        if DEBUG: print(f'all files: {file_list}')
        self.filter_all(file_list)
        if DEBUG: print(f'filtered file list: {self.files_list}')
        for file in self.files_list:
            self.move_file(file)

    def add_file_types(self, new_file_types: List[str]) -> None:
        # if not isinstance(new_file_types, List):
        #     pass
        for element in new_file_types:
            if isinstance(element, list):
                for file_type in element:
                    self.file_types.append(file_type)
            else:
                self.file_types.append(element)

    def add_valid_name(self, new_file_names: List[str]) -> None:
        self.valid_file_names.append(new_file_names)
