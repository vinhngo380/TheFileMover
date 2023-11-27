import os, shutil
from typing import List, Tuple
from pathlib import PurePath, Path
from glob import glob


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
                 valid_file_types: List[List[str]],
                 valid_file_names: List[str],
                 formatter='_', 
                 sub_dir=[]
                 ):
        self.folder_name = folder_name
        self.source_directory = source_directory
        self.target_directory = PurePath(os.path.normpath(os.path.join(target_directory, folder_name)))
        self.files_list = []
        self.valid_file_types = []
        self.add_file_types(valid_file_types)
        self.formatter = formatter
        self.sub_dir = sub_dir
        self.valid_file_names = []
        self.add_valid_names(valid_file_names)

    def string_to_tuple(self, dir: str) -> Tuple[str]:
        if DEBUG: print(f"directory_to_list: {os.path.normpath(dir)}")
        path_object_dir = PurePath(os.path.normpath(dir))
        return path_object_dir.parts[1::]
    
    def tuple_to_string(self, dir: Tuple[str]) -> str:
        path_object_dir = os.path.normpath(os.path.join(*dir))
        return path_object_dir
    
    def create_new_directories(self, directory: PurePath) -> None:
        temp = Path(directory)
        temp.mkdir(parents=True, exist_ok=True)
        print(f"create_new_directories: {directory}")

    def filter_by_name(self, files: List[str]) -> List[str]:
        #use glob.glob(valid_file_name.*?)
        files_filtered = []
        for file in files:
            file_name_list = file.split(self.formatter)[0]
            if DEBUG: print(f"file = {file_name_list} file_name = {self.valid_file_names}")
            if file_name_list in self.valid_file_names:
                files_filtered.append(file)
        return files_filtered
    
    def filter_by_type(self, files: List[str]) -> List[str]:
        #use glob.glob(*.file_type?)
        files_filtered = []
        for file in files:
            file_type = file.split('.')[-1].lower()
            if DEBUG: print(f"file = {file} file_type = {file_type} file_type type = {type(file_type)} conditional: {file_type in self.valid_file_names}")
            if file_type in self.valid_file_names:
                files_filtered.append(file)
        return files_filtered
    
    def filter_all(self, files) -> None:
        #use glob.glob (valid_file.name[formatter]*.file_type?)
        temp = self.filter_by_name(files)
        if DEBUG: print(f"filter_all: filtered by name = {temp}")
        self.files_list = self.filter_by_type(temp)
    
    def move_file(self, file: str) -> None:
        new_path = os.path.join(self.target_directory, file)
        print(f"move_file: source_dir = {self.source_directory} type = {type(self.source_directory)}", *self.source_directory.parts)
        unformatted_path = os.path.join(*self.source_directory.parts, file)
        formatted_path = os.path.normpath(unformatted_path)
        file_path = PurePath(formatted_path)
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
        for element in new_file_types:
            print(f"add file types: {element, new_file_types, not isinstance(element, List)}")
            if not isinstance(element, List):
                self.valid_file_types.append(element)
            else:
                self.add_file_types(element)

    def add_valid_names(self, new_file_names: List[str]) -> None:
        for element in new_file_names:
            print(f"add file types: {element, new_file_names, not isinstance(element, List)}")
            if not isinstance(element, List):
                self.valid_file_names.append(element)
            else:
                self.add_valid_names(element)
